def palindrome_of_length_at_least_n(text):
    """
    Returns the set of all palindromes of the length greater than or equal to 5 that exist in the given string.
    """
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 5, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes