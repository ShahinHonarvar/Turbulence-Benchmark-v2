from itertools import permutations

def palindromes_between_indices(s):
    English_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 9):
        for j in permutations(s[1:9], i):
            word = ''.join(j)
            if set(word).issubset(English_letters):
                palindromes.add(word.lower())
    return palindromes