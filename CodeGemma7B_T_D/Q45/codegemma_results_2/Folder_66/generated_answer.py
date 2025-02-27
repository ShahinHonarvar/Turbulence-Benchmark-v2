from itertools import permutations

def palindromes_between_indices(txt):
    unique_chars = set(txt[0:6].lower())
    radius = 2
    while True:
        permutations_with_radius = permutations(unique_chars, radius)
        palindrome_candidates = [''.join(p) for p in permutations_with_radius]
        if palindrome_candidates:
            return set(palindrome_candidates)
        radius += 1