from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [ch for ch in 'abcdefghijklmnopqrstuvwxyz']
    index_1_to_6 = s[1:7]
    palindromes_set = set()
    for p in permutations(index_1_to_6, 7):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes_set.add(word.lower())
    return palindromes_set