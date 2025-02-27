from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    english_letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for length in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes