from collections import defaultdict

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_of_specific_lengths(text):
    start, end = (32, 79)
    min_length, max_length = (35, 41)
    if end - start + 1 < min_length:
        return set()
    substr = text[start:end + 1]
    if len(substr) == 0:
        return set()
    min_start, max_end = (start + min_length - 1, start + max_length - 1)
    palindromes = set()
    for i in range(min_start, max_end + 1):
        for j in range(i, min(i - start + 1, end - i + 1) + min_length - 1):
            if is_palindrome(substr[i - j:i + j + 1]) and j - i >= min_length - 1:
                palindromes.add(substr[i - j:i + j + 1])
    return palindromes