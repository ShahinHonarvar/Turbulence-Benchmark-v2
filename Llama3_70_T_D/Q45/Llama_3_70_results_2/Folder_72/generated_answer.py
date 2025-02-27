from itertools import permutations

def palindromes_between_indices(s):
    letters = s[1:8].lower()
    valid_chars = 'abcdefghijklmnopqrstuvwxyz'
    letters = [char for char in letters if char in valid_chars]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes