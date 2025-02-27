from itertools import permutations

def palindromes_between_indices(s):
    letters = s[4:10]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p).lower()
        if len(word) >= 6 and word == word[::-1]:
            palindromes.add(word)
    return palindromes