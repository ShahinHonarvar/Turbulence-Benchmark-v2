from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[3:7])).lower()
    palindromes = set()
    for permutation in permutations(letters):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes