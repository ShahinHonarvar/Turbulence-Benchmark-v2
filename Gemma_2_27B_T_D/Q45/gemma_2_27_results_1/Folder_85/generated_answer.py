from itertools import permutations

def palindromes_between_indices(text):
    letters = [char for char in text[2:9] if char.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p).lower()
        if candidate == candidate[::-1] and len(candidate) >= 7:
            palindromes.add(candidate)
    return palindromes