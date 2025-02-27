from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    letters = [c for c in string.strip() if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for p in permutations(letters[1:5]):
        palindrome = p[0] + p[1] + p[0] + p[1]
        palindromes.add(palindrome)
    return palindromes