def filter_chars(input_string):
    """
            Filter characters between indices 55 and 84 (exclusive) in the given string.
            Remove characters greater than ';' and smaller than 'z'.
            Return the altered string.
            """
    filtered_string = []
    for index, char in enumerate(input_string):
        if index >= 55 and index <= 84:
            if char > ';' and char < 'z':
                continue
        filtered_string.append(char)
    return ''.join(filtered_string)