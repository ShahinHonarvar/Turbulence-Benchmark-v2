def return_n_smallest_chars(string):
    """
            Returns a list of the n smallest characters in a string.

            Args:
                string: The string to be sorted.

            Returns:
                A list of the n smallest characters in the string, sorted in descending order.
            """

    def get_ascii_value(char):
        """
                Returns the ASCII value of a character.

                Args:
                    char: The character to get the ASCII value of.

                Returns:
                    The ASCII value of the character.
                """
        return ord(char)

    def sort_by_ascii_value(char_a, char_b):
        """
                Sorts two characters by their ASCII values.

                Args:
                    char_a: The first character to compare.
                    char_b: The second character to compare.

                Returns:
                    -1 if char_a has a smaller ASCII value than char_b, 1 if char_b has a smaller ASCII value than char_a, or 0 if their ASCII values are equal.
                """
        return get_ascii_value(char_a) - get_ascii_value(char_b)
    sorted_string = sorted(string, key=sort_by_ascii_value, reverse=True)
    return sorted_string[:13]