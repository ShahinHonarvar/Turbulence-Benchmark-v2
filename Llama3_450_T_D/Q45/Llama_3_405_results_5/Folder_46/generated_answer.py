import itertools

def palindromes_between_indices(s):
    English_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    string = ''.join(filter(lambda x: x.lower() in English_alphabets, s[4:10]))
    unique_chars = ''.join(set(string.lower()))
    palindromes = set()
    for r in range(6, len(string) + 1):
        for perm in itertools.permutations(unique_chars, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes