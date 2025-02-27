import itertools

def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindromes = set()
    for i in range(4, len(s) + 1):
        for perm in itertools.permutations(s, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes