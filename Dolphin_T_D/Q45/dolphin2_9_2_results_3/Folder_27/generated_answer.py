import string
    import itertools

def palindromes_between_indices(s):
    sub_string = s[2:9]
    sub_string = ''.join([c for c in sub_string if c.isalpha()])
    sub_string = sub_string.lower()
    palindromes = set()
    for L in range(6, len(sub_string) + 1):
        for p in itertools.permutations(sub_string, L):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes