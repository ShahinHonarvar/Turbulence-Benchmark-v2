def palindrome_of_length_at_least_n(text: str) -> set[str]:
    """
            This function returns the set of all palindromes of the length greater than or equal to 13 that exist in the given text.
            """
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 13, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes