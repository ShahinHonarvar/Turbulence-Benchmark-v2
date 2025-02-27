from itertools import permutations

def palindromes_between_indices(string):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    s = set()
    for arr in permutations(string[:7].lower()):
        word = ''.join(arr)
        if word == word[::-1] and len(word) >= 5:
            for letter in alph:
                word = word.replace(letter.lower(), '').replace(letter.upper(), '')
            s.add(word)
    return s