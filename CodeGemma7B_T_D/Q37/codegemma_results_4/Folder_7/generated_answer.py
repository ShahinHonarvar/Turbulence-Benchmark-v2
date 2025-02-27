def filter_chars(s):
    """
    Write a function called 'filter_chars' that takes one argument, a string.
    For each character of the given string that occurs between indices 521 and 722, both inclusive, and is greater than or equal to character '>' and smaller than or equal to character '_', the function should remove all occurrences of that character from the string, while preserving the order of all characters in the string.
    The function should return the altered string.
    """
    return ''.join((c for c in s if c < '>' or c > '_'))