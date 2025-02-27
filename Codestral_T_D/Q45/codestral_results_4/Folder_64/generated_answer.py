from itertools import permutations

def palindromes_between_indices(s):
    sub_s = s[4:10].lower()
    palindromes = set()
    for i in range(5, len(sub_s) + 1):
        perms = permutations(sub_s, i)
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes