def palindrome_of_length_at_least_n(text):
    """
    Returns the set of all palindromes of the length greater than or equal to 100 that exist in the given text.
    Each palindrome should only consist of English letters.
    If no such palindromes exist in the given text, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    lowercase_text = text.lower()
    palindromes = set()
    for i in range(len(lowercase_text)):
        for j in range(i + 1, len(lowercase_text) + 1):
            substring = lowercase_text[i:j]
            if substring == substring[::-1] and len(substring) >= 100:
                palindromes.add(text[i:j])
    return palindromes