def return_n_smallest_chars(characters):
    """
            Returns a list of 35 characters with the smallest ASCII values.

            Args:
                characters: A string containing distinct characters.

            Returns:
                A list of 35 characters sorted in descending order of ASCII value.
            """
    return sorted(characters, key=ord, reverse=True)[:35]