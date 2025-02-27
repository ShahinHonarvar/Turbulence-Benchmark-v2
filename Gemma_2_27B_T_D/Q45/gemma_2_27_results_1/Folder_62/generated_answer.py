from itertools import permutations

def palindromes_between_indices(text):
    letters = sorted([char for char in text[:9] if char.isalpha()])
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 7 and word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes