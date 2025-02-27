from itertools import permutations

def palindromes_between_indices(text):
    indexes = range(4, 7)
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    alphabets = text[indexes[0]:indexes[-1] + 1]
    alphabets_set = set(alphabets)
    if not alphabets_set.issubset(english_letters):
        return palindromes
    for i in permutations(alphabets):
        if ''.join(i) in english_letters and text[indexes[0]] == i[len(i) // 2] and (text[indexes[-1]] == i[len(i) // 2]):
            palindromes.add(''.join(i).lower())
    return palindromes