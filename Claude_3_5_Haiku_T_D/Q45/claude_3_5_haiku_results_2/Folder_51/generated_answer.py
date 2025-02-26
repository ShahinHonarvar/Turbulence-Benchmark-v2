from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6] if c.isalpha()]
    palindrome_set = set()

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 3 and len(current) == len(chars) * 2 - len(current):
                palindrome_set.add(''.join(current))
                return
            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i - 1]:
                    continue
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i + 1:])
                current.pop()
        for perm in set(permutations(chars)):
            backtrack([], list(perm))
    generate_palindromes(letters)
    return palindrome_set