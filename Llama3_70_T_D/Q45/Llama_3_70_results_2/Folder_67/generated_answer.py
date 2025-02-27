from itertools import permutations

def palindromes_between_indices(s):
    sub_string = ''.join(filter(str.isalpha, s[2:7])).lower()
    palindromes = set()
    for r in range(5, len(sub_string) + 1):
        for perm in set(permutations(sub_string, r)):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes