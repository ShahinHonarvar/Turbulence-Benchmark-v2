from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:8] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            test_perm = list(perm)
            if test_perm == test_perm[::-1]:
                palindrome = ''.join(test_perm)
                palindromes.add(palindrome)
    return palindromes