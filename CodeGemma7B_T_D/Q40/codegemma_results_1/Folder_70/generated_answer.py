def return_n_smallest_chars(text):
    """
            Returns a list of the smallest two characters in a string.

            Args:
                text: A string of distinct characters.

            Returns:
                A list of exactly two characters of the given string that have the smallest ASCII values.
            """
    characters = sorted(text, key=ord, reverse=True)
    return characters[:2]