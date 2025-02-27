def palindrome_of_length_n(text):
    """
    Returns the set of all palindromes of the length equal to 173.
    """
    result = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 173, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                result.add(substring.capitalize())
    return result