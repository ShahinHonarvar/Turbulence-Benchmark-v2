from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_string = s[0:3]
    palindromes = set()
    for perm in permutations(sub_string, 3):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes