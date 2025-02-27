from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[1:9]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(6, len(s) + 1):
        for p in permutations(s, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes