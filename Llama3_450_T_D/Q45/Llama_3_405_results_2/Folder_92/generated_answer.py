import itertools

def palindromes_between_indices(s):
    substring = s[4:8]
    letters = [c for c in substring if c.isalpha()]
    letters = [c.lower() for c in letters]
    unique_letters = set(letters)
    palindromes = set()
    for r in range(2, len(unique_letters) + 1):
        for combination in itertools.combinations(unique_letters, r):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation) + ''.join(permutation[::-1])
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes