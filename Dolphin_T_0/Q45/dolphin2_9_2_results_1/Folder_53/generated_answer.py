import itertools

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[4:9]))
    palindromes = set()
    for p in range(6, len(substring) + 1):
        for h in itertools.combinations(substring, p):
            if ''.join(h) == ''.join(h)[::-1]:
                palindromes.add(''.join(h).lower())
    return palindromes