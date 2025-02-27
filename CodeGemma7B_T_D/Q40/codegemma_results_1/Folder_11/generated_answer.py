def return_n_smallest_chars(string):
    """
        Return a list of n smallest characters of a string sorted in ascending order of their ASCII values.

        Args:
        string: A string of distinct characters.

        Returns:
        A list of n smallest characters of the given string sorted in ascending order.
        """

    def get_ascii_values(string):
        """
            Create a dictionary of characters and their ASCII values.

            Args:
            string: A string of characters.

            Returns:
            A dictionary of characters and their ASCII values.
            """
        return {char: ord(char) for char in string}

    def get_smallest_chars(ascii_values, n):
        """
            Return a list of n smallest characters from a dictionary of characters and their ASCII values.

            Args:
            ascii_values: A dictionary of characters and their ASCII values.
            n: The number of smallest characters to return.

            Returns:
            A list of n smallest characters from the given dictionary.
            """
        return sorted(ascii_values.keys(), key=ascii_values.get)[:n]
    ascii_values = get_ascii_values(string)
    smallest_chars = get_smallest_chars(ascii_values, 17)
    return smallest_chars