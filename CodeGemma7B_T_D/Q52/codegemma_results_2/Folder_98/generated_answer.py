def palindrome_of_length_n(text):
    """
    This function takes in a string and returns the set of all palindromes of length 6 that are substrings of the string.
    The function finds the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    for i in range(len(text) - 5):
        for j in range(i + 1, len(text) - 4):
            palindrome = text[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes