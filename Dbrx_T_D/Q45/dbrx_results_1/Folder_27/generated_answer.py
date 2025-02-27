from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = [c for c in s[2:9] if c.isalpha()]
    if len(english_letters) < 6:
        return set()
    palindrome_set = set()
    for i in range(6, len(english_letters) + 1):
        current_combinations = itertools.combinations(english_letters, i)
        for combination in current_combinations:
            if is_palindrome(combination):
                palindrome_set.add(''.join(combination))
    return palindrome_set

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]