import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[7:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    letters_set = set(letters)
    palindromes = set()
    for r in range(2, len(letters) + 1):
        for combination in itertools.combinations(letters_set, r):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation) + ''.join(permutation)[::-1]
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes