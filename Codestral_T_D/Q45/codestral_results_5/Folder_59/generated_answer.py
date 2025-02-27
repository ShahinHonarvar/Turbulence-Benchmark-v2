from itertools import permutations

def palindromes_between_indices(s):
    letters = s[8:10].lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes