import itertools

def palindromes_between_indices(s):
    s = s[2:8].lower()
    palindromes = set()
    for L in range(6, len(s) + 1):
        for perm in itertools.permutations(s, L):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes