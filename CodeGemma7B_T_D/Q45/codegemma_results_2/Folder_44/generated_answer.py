from itertools import permutations

def palindromes_between_indices(word):
    palindromes = set()
    word = word[2:7 + 1]
    if len(word) >= 3:
        for letters in permutations(word):
            letters = ''.join(letters)
            if letters == letters[::-1]:
                palindromes.add(set(letters))
    return palindromes