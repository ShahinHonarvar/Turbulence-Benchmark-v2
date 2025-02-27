def filter_chars(txt):
    """This function takes one argument, a string.
    For each character of the given string that occurs between indices 19 and 92, both inclusive, and is greater than or equal to character '8' and smaller than or equal to character 'm', the function should remove all occurrences of that character from the string, while preserving the order of all characters in the string.
    The function should return the altered string."""
    new_txt = ''
    for i, char in enumerate(txt):
        if not (19 <= i <= 92 and char >= '8' and (char <= 'm')):
            new_txt += char
    return new_txt