from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    subsequence = s[2:5].lower()
    valid_chars = [char for char in subsequence if char.isalpha()]
    palindromes = set()
    perms = set(permutations(valid_chars, len(valid_chars)))
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes