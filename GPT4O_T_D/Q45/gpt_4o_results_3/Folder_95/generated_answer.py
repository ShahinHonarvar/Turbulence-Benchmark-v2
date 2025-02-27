from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[7:9].lower()

    def is_palindrome(word):
        return word == word[::-1]
    char_count = Counter((c for c in substring if c.isalpha()))
    half_length_permutations = set()
    for perm in permutations(char_count.elements()):
        half_string = ''.join(perm)
        half_length_permutations.add(half_string)
    palindromes = set()
    for half in half_length_permutations:
        full = half + half[::-1] if len(half) * 2 >= 3 else ''
        if is_palindrome(full):
            palindromes.add(full)
    return palindromes