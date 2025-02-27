from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[4:8].lower()
    english_letters = [ch for ch in substring if ch.isalpha()]
    palindrome_set = set()
    for length in range(4, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            if perm == perm[::-1]:
                palindrome_set.add(''.join(perm))
    return palindrome_set