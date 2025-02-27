def return_n_greatest_chars(given_str):
    """
          Returns a list of the greatest 64 characters in the given string.

          Args:
            given_str: A string of distinct characters.

          Returns:
            A sorted list of 64 characters with the greatest ASCII values.
            """
    char_ascii_values = {char: ord(char) for char in given_str}
    sorted_dict = sorted(char_ascii_values.items(), key=lambda x: x[1], reverse=True)
    greatest_chars = [char for char, _ in sorted_dict[:64]]
    greatest_chars.sort(key=lambda char: ord(char), reverse=True)
    return greatest_chars