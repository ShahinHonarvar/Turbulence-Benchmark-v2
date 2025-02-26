from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindrome_set = set()
    for length in range(5, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for i in range(len(perm) - length + 1):
                candidate = perm[i:i + length]
                if list(candidate) == list(candidate)[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set