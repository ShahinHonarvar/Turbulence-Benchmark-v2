from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(3, len(letters) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if len(candidate) >= 3:
                    palindrome = candidate + candidate[::-1]
                    if len(set(palindrome)) >= 3:
                        palindromes.add(''.join(palindrome))
    return palindromes