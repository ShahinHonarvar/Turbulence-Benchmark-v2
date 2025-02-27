from collections import Counter

def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    start, end = (4, 8)
    if start < 0 or end >= len(s) or (not set(s[start:end + 1]).intersection(english_letters)):
        return set()
    palindromes = set()
    for substring in ''.join((char for char in s[start:end + 1] if char in english_letters)).lower().split():
        if len(substring) < 3:
            continue
        substring = ''.join(sorted(substring))
        palindrome = substring + substring[::-1][1:]
        palindromes.add(palindrome)
    return palindromes