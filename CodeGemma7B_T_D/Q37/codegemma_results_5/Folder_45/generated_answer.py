def filter_chars(str):
    """
    Write a function called 'filter_chars' that takes one argument, a string.
    For each character of the given string that occurs between indices 72 and 94, both inclusive,
    and is greater than or equal to character '.' and smaller than or equal to character 'b',
    the function should remove all occurrences of that character from the string,
    while preserving the order of all characters in the string.
    The function should return the altered string.
    """
    filtered_str = ''
    for i in range(len(str)):
        if i >= 72 and i <= 94 and (str[i] >= '.') and (str[i] <= 'b'):
            continue
        filtered_str += str[i]
    return filtered_str