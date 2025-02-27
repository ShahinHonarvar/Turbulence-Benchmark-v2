from itertools import permutations
    import string

def palindromes_between_indices(s):
    subset = ''.join(s[2:10])
    subset = ''.join((c for c in subset if c.isalpha()))
    subset = subset.lower()
    palindrome_set = set()
    for i in range(7, len(subset) + 1):
        for perm in permutations(subset, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindrome_set.add(word)
    return palindrome_set