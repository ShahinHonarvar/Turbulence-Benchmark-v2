def insert_before_character(an_iterator):
    """
            This function inserts a character in a string at the given location.

            Args:
                an_iterator: An iterator object that contains the string to be modified.

            Returns:
                A string that is identical except that character 'P' has been inserted
                immediately preceding any occurrences of character ' '.
            """
    result = []
    for char in an_iterator:
        if char == ' ':
            result.append('P')
        result.append(char)
    return ''.join(result)