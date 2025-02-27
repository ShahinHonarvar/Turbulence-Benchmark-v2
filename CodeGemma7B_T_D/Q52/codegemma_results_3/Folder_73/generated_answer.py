def palindrome_of_length_n(text):
    """
    Input: text (str)
    Output: set(str)
    """
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                palindromes.add(text[i:j + 1])
    return palindromes