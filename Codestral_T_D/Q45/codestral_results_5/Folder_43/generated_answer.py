from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6]
    s = s.lower()
    palindromes = set()
    for p in permutations(s):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes