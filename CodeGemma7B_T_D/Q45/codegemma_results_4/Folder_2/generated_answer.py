import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c in string.ascii_lowercase and 1 <= string.index(c) <= 5]
    palindrome_candidates = itertools.combinations_with_replacement(letters, 6)
    palindromes = set()
    for candidate in palindrome_candidates:
        candidate = ''.join(candidate)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes