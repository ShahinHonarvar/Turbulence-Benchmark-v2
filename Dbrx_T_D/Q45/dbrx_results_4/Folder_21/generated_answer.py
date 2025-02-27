from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = defaultdict(int)
    for i in range(1, 9):
        if s[i].isalpha():
            english_letters[s[i].lower()] += 1
    palindromes = set()
    for letters in map(''.join, itertools.product(english_letters.keys(), repeat=7)):
        if len(letters) == len(set(letters)) and letters == letters[::-1]:
            palindromes.add(letters)
    return palindromes