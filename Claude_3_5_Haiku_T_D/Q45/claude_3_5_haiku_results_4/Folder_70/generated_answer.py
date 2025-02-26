from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for start in range(len(perm) - length + 1):
                subset = perm[start:start + length]
                if list(subset) == list(subset)[::-1]:
                    palindrome = ''.join(subset)
                    if len(palindrome) >= 4:
                        palindromes.add(palindrome)
    return palindromes