import itertools

def palindromes_between_indices(text):
    letters = [char for char in text[2:10] if char.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters):
        candidate = ''.join(permutation).lower()
        if len(candidate) >= 7 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes