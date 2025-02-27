def palindrome_of_length_at_least_n(text):
    """
            Given a text, the function returns a set of palindromes of length greater than or equal to 48.
            """
    text = ''.join((ch for ch in text.lower() if ch.isalpha()))
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 24, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                palindromes.add(text[i:j + 1])
    return palindromes