def remove_repeat_chars(string):
    """
            Removes repeated characters at indices 13 through 70 of a string.

            Args:
            string: The input string.

            Returns:
            The string with repeated characters at indices 13 through 70 removed.
            """
    for i in range(13, 70):
        if string[i] in string[i + 1:]:
            while string[i] in string[i + 1:]:
                string = string[:i] + string[i + 1:]
    return string