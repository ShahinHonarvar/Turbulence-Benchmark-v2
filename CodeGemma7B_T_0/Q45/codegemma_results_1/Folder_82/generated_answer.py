from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(text):
    text = text.lower()
    if not text or len(text) < 7:
        return set()
    letters = [char for char in text if char in ascii_lowercase]
    if not letters or len(letters) < 7:
        return set()
    permutations_of_letters = set([''.join(p) for p in permutations(letters)])
    palindromes = set()
    for permutation in permutations_of_letters:
        if permutation == permutation[::-1]:
            palindromes.add(permutation)
    return palindromes