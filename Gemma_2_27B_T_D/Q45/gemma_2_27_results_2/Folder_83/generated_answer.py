from itertools import permutations

def palindromes_between_indices(text):
    letters = [letter for letter in text[2:10] if letter.isalpha()]
    palindromes = set()
    for permutation in permutations(letters):
        candidate = ''.join(permutation)
        if candidate.lower() == candidate.lower()[::-1] and len(candidate) >= 7:
            palindromes.add(candidate)
    return palindromes