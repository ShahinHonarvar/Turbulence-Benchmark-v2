from itertools import permutations

def palindromes_between_indices(s):
    s = s[:4].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes