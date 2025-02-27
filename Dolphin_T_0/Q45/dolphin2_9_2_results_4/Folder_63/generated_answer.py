from itertools import permutations, chain

def palindromes_between_indices(s):
    English_letters = 'abcdefghijklmnopqrstuvwxyz'
    s = s[0:4].lower().replace(' ', '')
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if any((letter in English_letters for letter in word)) and word == word[::-1]:
                palindromes.add(word)
    return palindromes