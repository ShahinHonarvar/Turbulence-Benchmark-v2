def palindrome_of_length_n(text):
    """True if text is a palindrome, False otherwise."""
    return text == text[::-1]

def palindrome_of_length_48(text):
    """Returns the set of all palindromes of the length equal to 48."""
    text = text.lower()
    palindromes = {text}
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if palindrome_of_length_n(text[i:j + 1]):
                palindromes.add(text[i:j + 1])
    return palindromes