from itertools import permutations

def palindromes_between_indices(s):
    s = s[:9].lower()
    english_letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for perm in permutations(english_letters, 7):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes