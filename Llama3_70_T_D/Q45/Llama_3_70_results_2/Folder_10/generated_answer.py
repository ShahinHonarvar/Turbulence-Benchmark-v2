from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(3, len(s) + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes