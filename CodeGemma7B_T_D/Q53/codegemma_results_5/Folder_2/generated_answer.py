def palindrome_of_length_at_least_n(text):
    """
    Returns the set of all palindromes of the length greater than or equal to 55 that exist in the given string.
    """
    lowercase_text = text.lower()
    valid_chars = set(string.ascii_lowercase)
    palindrome_set = set()
    for i in range(len(lowercase_text)):
        for j in range(i + 1, len(lowercase_text)):
            substring = lowercase_text[i:j + 1]
            if substring == substring[::-1] and set(substring).issubset(valid_chars) and (len(substring) >= 55):
                palindrome_set.add(substring)
    return palindrome_set