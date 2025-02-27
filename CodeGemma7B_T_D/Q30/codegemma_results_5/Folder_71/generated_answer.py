def insert_before_character(s):
    """
            Inserts 'S' before all '2' characters in a string.

            Args:
                s: The input string.

            Returns:
                The modified string with 'S' inserted before all '2' characters.
            """
    return ''.join(['S' + c if c == '2' else c for c in s])