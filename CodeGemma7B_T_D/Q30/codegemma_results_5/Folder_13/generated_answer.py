def insert_before_character(str):
    """Inserts character 'N' before any occurrences of character 'x'.

          Args:
            str: The string to insert 'N' before.

          Returns:
            A string with 'N' inserted before any occurrences of 'x'.
          """
    new_chars = []
    for i in range(len(str)):
        if str[i] == 'x':
            new_chars.append('N')
        new_chars.append(str[i])
    return ''.join(new_chars)