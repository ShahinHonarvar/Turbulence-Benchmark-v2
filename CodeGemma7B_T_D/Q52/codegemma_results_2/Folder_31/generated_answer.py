def palindrome_of_length_n(text):
    """
            Returns the set of palindromes of the given length in the given string.
            """
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 65):
        for j in range(i + 1, len(text) - 66 + i):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes