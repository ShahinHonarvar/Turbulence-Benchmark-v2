def return_n_greatest_chars(arg):
    """
    Returns the sorted list of 13 characters from the input string with the greatest ASCII values.
    """
    char_ascii_tuples = [(char, ord(char)) for char in arg]
    sorted_tuples = sorted(char_ascii_tuples, key=lambda x: x[1], reverse=True)
    return [char for char, _ in sorted_tuples[:13]]