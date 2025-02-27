from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    english_letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(english_letters):
        candidate = ''.join(perm)
        if len(candidate) >= 6 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes