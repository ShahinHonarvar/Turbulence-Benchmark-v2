import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:8] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combination in itertools.combinations(letters, r):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes