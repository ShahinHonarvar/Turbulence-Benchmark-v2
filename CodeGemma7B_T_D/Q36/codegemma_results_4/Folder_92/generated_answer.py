def filter_chars(string):
    """
            Filters out characters between indices 1 and 6 (exclusive), leaving those greater than ',' and smaller than 'f' intact.

            Args:
                string: The input string.

            Returns:
                The filtered string.
            """
    for i in range(1, 6):
        char = string[i]
        if char > ',' and char < 'f':
            string = string.replace(char, '')
    return string