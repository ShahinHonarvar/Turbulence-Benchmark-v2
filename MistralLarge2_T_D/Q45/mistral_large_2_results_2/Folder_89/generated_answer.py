from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[5:10].lower()))
    palindromes = set()
    for length in range(6, len(substring) + 1):
        for p in permutations(substring, length):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes