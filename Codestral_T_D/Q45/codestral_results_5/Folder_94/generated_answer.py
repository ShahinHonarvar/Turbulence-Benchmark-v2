from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:5].lower()
    palindromes = set()
    for p in permutations(s):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes