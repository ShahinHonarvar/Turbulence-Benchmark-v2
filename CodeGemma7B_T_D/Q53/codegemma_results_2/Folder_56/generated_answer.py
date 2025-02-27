def palindrome_of_length_at_least_n(text):
    """
    Finds all palindromes of the length greater than or equal to 84 that exist in a string.
    The function returns an empty set if no such palindromes exist in the given string.
    """
    text = text.lower()
    palindrome_set = set()
    for i in range(len(text)):
        for j in range(i + 84, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set