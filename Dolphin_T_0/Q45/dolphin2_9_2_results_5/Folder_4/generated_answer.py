from itertools import permutations

def palindromes_between_indices(s):
    sub_s = s[3:10].lower()
    sub_s = ''.join(sorted(sub_s))
    palindromes = set()
    for p in permutations(sub_s, 7):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes