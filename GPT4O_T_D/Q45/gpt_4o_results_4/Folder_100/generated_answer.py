from itertools import permutations

def palindromes_between_indices(s):
    chars = s[:6].lower()
    filtered_chars = [c for c in chars if c.isalpha()]
    palindromes = set()
    for p in permutations(filtered_chars, len(filtered_chars)):
        if len(p) >= 6 and p == p[::-1]:
            palindromes.add(''.join(p))
    return palindromes