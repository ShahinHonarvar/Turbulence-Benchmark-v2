import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(0, 6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    perms = set([''.join(p) for p in itertools.permutations(letters)])
    palindromes = set()
    for perm in perms:
        if len(perm) >= 6 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes