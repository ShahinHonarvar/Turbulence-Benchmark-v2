def return_n_greatest_chars(str):
    """
                The function takes one argument, `str`, a string of distinct characters.
                It returns the sorted list of 36 characters of the given string
                that have the greatest ASCII values.
                """
    str = str[:36]
    return sorted(str, key=ord)