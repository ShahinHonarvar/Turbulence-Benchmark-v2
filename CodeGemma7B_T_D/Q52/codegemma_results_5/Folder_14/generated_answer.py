def palindrome_of_length_n(string):
    """
            Checks whether a given string contains palindromes of length 63 and returns a set of all such palindromes in a case-insensitive manner.

            Parameters:
            string: The input string to search for palindromes in.

            Returns:
            A set of palindromes of length 63 from the input string.
            """

    def is_palindrome(word):
        """
                Checks if a given word is a palindrome.

                Parameters:
                word: The word to check for palindromic symmetry.

                Returns:
                True if the word is a palindrome, False otherwise.
                """
        return word == word[::-1]
    processed_string = ''.join((c.lower() for c in string if c.isalpha()))
    palindromes = set()
    for start in range(len(processed_string) - 62):
        for end in range(start + 63, len(processed_string) + 1):
            substring = processed_string[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes