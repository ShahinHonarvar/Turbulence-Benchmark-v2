from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substr = s[3:5].lower()
    letters = [char for char in substr if char.isalpha()]
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes