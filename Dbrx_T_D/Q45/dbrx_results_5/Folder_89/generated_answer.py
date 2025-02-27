from itertools import permutations

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = s[5:10]
    palindromes = set()
    for i in range(6, len(substring) + 1):
        for perm in permutations(substring, i):
            candidate = ''.join(perm)
            if candidate[0] in english_letters and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes