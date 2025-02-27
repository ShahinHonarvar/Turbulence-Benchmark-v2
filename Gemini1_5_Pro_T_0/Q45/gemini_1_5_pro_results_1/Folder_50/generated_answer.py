import itertools

def palindromes_between_indices(string):
    s = string[4:9].lower()
    letters = [char for char in s if char.isalpha()]
    permutations = set([''.join(p) for p in itertools.permutations(letters)])
    palindromes = set()
    for p in permutations:
        if len(p) >= 5 and p == p[::-1]:
            palindromes.add(p)
    return palindromes