def palindrome_of_length_at_least_n(text):
    """
    Returns the set of all palindromes of the length greater than or equal to 22
    that exist in the given string. Each palindrome should only consist of
    English letters. If no such palindromes exist in the given string,
    the function should return an empty set. The function should find the
    palindromes in a case-insensitive manner.
    """
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 22, len(text) + 1):
            if text[i:j] == text[j - 2:i - 2:-1]:
                palindromes.add(text[i:j])
    return palindromes