from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    unique_letters = set(letters)
    if len(unique_letters) < 4:
        return set()
    palindromes = set()
    for p in permutations(unique_letters, 7):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes