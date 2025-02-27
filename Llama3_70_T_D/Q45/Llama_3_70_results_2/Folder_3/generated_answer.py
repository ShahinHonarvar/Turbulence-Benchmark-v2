import itertools

def palindromes_between_indices(s):
    substring = s[7:10].lower()
    substring = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for r in range(3, len(substring) + 1):
        for p in itertools.permutations(substring, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes