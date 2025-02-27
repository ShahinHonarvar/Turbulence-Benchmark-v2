def palindrome_of_length_n(text):
    """Find all palindromes of the given length in the given text."""
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 92 + 1):
        substring = text[i:i + 92]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes