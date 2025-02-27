from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = ''.join(filter(str.isalpha, s[1:8]))
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes