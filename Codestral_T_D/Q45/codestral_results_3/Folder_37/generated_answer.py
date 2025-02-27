from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindromes = set()
    for i in range(5, 0, -1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 5:
                palindromes.add(word)
    return palindromes