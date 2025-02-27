from itertools import permutations

def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[4:9]] if 4 <= 8 < len(s) else []
    palindromes = set()
    for p in permutations(letters, 3):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes