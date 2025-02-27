from itertools import permutations

def palindromes_between_indices(text):
    letters = text[2:9]
    english_letters = [letter for letter in letters if letter.isalpha()]
    palindromes = set()
    for p in permutations(english_letters):
        candidate = ''.join(p).lower()
        if len(candidate) >= 7 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes