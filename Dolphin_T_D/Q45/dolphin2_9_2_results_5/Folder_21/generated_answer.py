from itertools import permutations

def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    s = s[1:9].lower()
    palindromes = set()
    for p in permutations(s, len(s)):
        word = ''.join(p)
        if word == word[::-1] and any((c in english_letters for c in word)) and (len(word) >= 7):
            palindromes.add(word)
    return palindromes