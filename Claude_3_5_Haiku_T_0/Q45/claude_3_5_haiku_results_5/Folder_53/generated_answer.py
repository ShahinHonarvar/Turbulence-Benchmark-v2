from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(6, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if len(candidate) >= 6:
                    palindrome = candidate + candidate[::-1]
                    if len(palindrome) % 2 == 0:
                        unique_palindromes.add(''.join(palindrome))
    return unique_palindromes