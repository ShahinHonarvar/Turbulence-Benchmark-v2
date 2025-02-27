def palindrome_of_length_at_least_n(string):
    """
        Finds all palindromes of length greater than or equal to 29 in a given string.

        Args:
            string: The input string.

        Returns:
            A set of all palindromes of length greater than or equal to 29 that exist in the given string, or an empty set if no such palindromes exist.
        """
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j] and len(string[i:j + 1]) >= 29:
                palindromes.add(string[i:j + 1])
    return palindromes