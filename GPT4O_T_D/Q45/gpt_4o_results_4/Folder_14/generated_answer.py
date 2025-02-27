from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 6 or not any((c.isalpha() for c in s[4:6])):
        return set()
    substr = ''.join(filter(str.isalpha, s[4:6]))
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for perm in permutations(substr, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes