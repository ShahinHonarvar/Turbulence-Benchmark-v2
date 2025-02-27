from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    sub = s[2:5]
    letters = [c.lower() for c in sub if c.isalpha()]
    if len(letters) < 2:
        return set()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        string = ''.join(perm)
        if string == string[::-1] and len(string) >= 4:
            palindromes.add(string)
    return palindromes