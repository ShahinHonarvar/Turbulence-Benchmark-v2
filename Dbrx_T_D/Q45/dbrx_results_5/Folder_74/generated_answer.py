import re
    from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for start in range(1, 6):
        for end in range(start + 5, min(6, len(s))):
            substr = s[start:end + 1]
            if set(substr) <= english_letters:
                reversed_substr = substr[::-1]
                if substr.lower() == reversed_substr.lower():
                    palindromes.add(substr)
    return palindromes