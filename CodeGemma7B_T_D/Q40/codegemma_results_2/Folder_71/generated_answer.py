def return_n_smallest_chars(text):
    """
            Returns a list of 14 characters from the given string with the smallest ASCII values.

            Args:
            text: A string of distinct characters.

            Returns:
            A list of 14 characters sorted in ascending order of ASCII values.
            """
    char_ascii_tuples = [(char, ord(char)) for char in text]
    char_ascii_tuples.sort(key=lambda x: x[1])
    return [char for char, _ in char_ascii_tuples[:14]]