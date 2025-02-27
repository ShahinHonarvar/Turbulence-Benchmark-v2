def palindrome_of_length_n(text):
    """
            This function finds all palindromes of the length equal to 186, where each palindrome is a substring of the given string.
            The function iterates over all the possible substrings of the given string and checks if they are palindromes.
            The function also finds the palindromes in a case-insensitive manner.
            """

    def is_palindrome(substring):
        """
                This function checks if a given substring is a palindrome.
                """
        return substring == substring[::-1]
    palindromes = set()
    for i in range(len(text) - 185):
        for j in range(i + 186):
            substring = text[i:j]
            if is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes