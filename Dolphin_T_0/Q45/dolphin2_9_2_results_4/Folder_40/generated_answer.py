import itertools

def palindromes_between_indices(s):
    string_between = s[4:10]
    letters = [ch for ch in string_between if ch.isalpha()]
    palindromes = set()
    for i in range(7, len(letters) + 1):
        perms = itertools.permutations(letters, i)
        for perm in perms:
            for p in set(perm):
                if p == p[::-1]:
                    palindromes.add(p.lower())
                    palindromes.add(p.upper())
    return palindromes