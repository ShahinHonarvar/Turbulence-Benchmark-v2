from itertools import permutations

def palindromes_between_indices(s):
    s = s[:5].lower()
    english_letters = [char for char in s if char.isalpha()]
    palindromes_set = set()
    for r in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes_set.add(word)
    return palindromes_set