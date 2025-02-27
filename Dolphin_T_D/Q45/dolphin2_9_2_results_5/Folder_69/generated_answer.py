from itertools import permutations

def palindromes_between_indices(s):
    s = s[:4].lower()
    lens = len(s)
    palindromes = set()
    for p in permutations(s, lens):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes if palindromes else set()