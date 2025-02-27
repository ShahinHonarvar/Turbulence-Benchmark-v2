import itertools

def palindromes_between_indices(s):
    string = s[3:9]
    palindromes_set = set()
    for i in range(6, len(string) + 1):
        for p in itertools.permutations(string, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes_set.add(word.lower())
    return palindromes_set