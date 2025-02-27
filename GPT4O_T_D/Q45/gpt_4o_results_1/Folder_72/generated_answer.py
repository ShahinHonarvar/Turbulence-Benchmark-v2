from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    sub_str = s[1:8].lower()
    letters = [ch for ch in sub_str if ch.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if len(word) >= 6 and word == word[::-1]:
            palindromes.add(word)
    return palindromes