from itertools import permutations

def palindromes_between_indices(s):
    sub_s = s[7:10].lower()
    palindromes = set()
    for i in range(4, len(sub_s) + 1):
        for p in permutations(sub_s, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes