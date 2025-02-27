from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join((s[i] for i in range(7)))
    substring = ''.join(filter(str.isalpha, substring)).lower()
    subs = set(substring)
    subs = {i: subs.count(i) for i in subs}
    palindromes = set()
    for p in range(3, len(substring) + 1):
        for i in permutations(subs.items(), p):
            word = ''.join([ii for iii, ii in i for _ in range(iii)])
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes