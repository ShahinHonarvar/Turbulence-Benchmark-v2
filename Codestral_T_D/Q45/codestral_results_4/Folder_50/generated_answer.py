from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    letters = [char.lower() for char in string[4:9] if char.isalpha()]
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes