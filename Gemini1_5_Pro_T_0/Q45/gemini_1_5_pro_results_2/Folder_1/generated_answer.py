import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(4, 8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    permutations = set([''.join(p) for p in itertools.permutations(letters)])
    palindromes = set()
    for p in permutations:
        if len(p) >= 5 and p == p[::-1]:
            palindromes.add(p)
    return palindromes