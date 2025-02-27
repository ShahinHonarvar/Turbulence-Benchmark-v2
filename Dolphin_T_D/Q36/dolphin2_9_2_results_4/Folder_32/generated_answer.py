def filter_chars(s):
    """
    Running the function filter_chars with the input string 'Hello! How are you, alive? God knows!' it will keep all characters in the same order while removing all occurrences of a character found between indices 40-63 and greater than '7' and smaller than 'H'.
    """
    for i in range(40, 63):
        if '7' < s[i] < 'H':
            s = s.replace(s[i], '')
    return s