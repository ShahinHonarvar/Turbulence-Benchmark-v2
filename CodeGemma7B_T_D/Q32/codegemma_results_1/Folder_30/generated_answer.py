def insert_after_character(str):
    """
            Inserts 'F' after every '4' in a string.

            Parameters:
            str: The input string.

            Returns:
            A new string with 'F' inserted after every '4'.
            """
    return ''.join((c + 'F' if c == '4' else c for c in str))