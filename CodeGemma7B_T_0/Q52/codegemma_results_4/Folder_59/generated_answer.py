def palindrome_of_length_n(text):
    """
    This function takes a string and returns the set of all palindromes of the length equal to 39,
    where each palindrome is a substring of the given string. Each palindrome should only consist
    of English letters. If there is no palindrome of the specified length as a substring of
    the given string, the function should return an empty set. The function should find the
    palindromes in a case-insensitive manner.
    """
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 38):
        for j in range(i + 1, len(text) - 38 + i + 1):
            if text[i:j + 1] == text[j:i - 1:-1]:
                palindromes.add(text[i:j + 1])
    return palindromes