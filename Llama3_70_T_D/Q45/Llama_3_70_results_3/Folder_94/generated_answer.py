from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:5].lower()
    if len(s) == 0:
        return set()
    elif len(s) == 1:
        return set() if len(s) < 3 else {s}
    else:
        palindromes = set()
        for p in permutations(s):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 3:
                palindromes.add(word)
        return palindromes