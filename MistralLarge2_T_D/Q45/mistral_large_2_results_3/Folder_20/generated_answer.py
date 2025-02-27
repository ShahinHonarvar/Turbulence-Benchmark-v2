from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[2:9])).lower()
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for p in permutations(substring, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes