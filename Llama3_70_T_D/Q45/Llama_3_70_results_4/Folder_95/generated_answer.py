from itertools import permutations

def palindromes_between_indices(s):
    s = s[7:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = ''.join(filter(lambda x: x in english_letters, s))
    palindromes = set()
    for r in range(3, len(s) + 1):
        for perm in permutations(s, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes