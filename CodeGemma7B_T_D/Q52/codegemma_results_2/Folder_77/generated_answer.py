import re

def palindrome_of_length_n(text):
    """Finds all palindromes of the length equal to 173 as substrings of the given string."""
    patterns = []
    for i in range(len(text)):
        for j in range(i + 173, len(text) + 1):
            patterns.append(text[i:j])
    palindromes = set()
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            palindromes.add(pattern)
    return palindromes