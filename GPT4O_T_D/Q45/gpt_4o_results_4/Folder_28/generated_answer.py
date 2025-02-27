from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    english_letters = [char.lower() for i, char in enumerate(s) if i in range(1, 6) and char.isalpha()]
    palindromes = set()
    for perm in permutations(english_letters):
        for length in range(4, len(perm) + 1):
            substr = ''.join(perm[:length])
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes