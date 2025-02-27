from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()[3:5]
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes