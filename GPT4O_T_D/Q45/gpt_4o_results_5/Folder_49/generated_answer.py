from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[5:8].lower()
    english_letters = [char for char in substring if char.isalpha()]
    if len(english_letters) < 3:
        return set()
    palindrome_set = set()
    for perm in permutations(english_letters):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindrome_set.add(candidate)
    return palindrome_set