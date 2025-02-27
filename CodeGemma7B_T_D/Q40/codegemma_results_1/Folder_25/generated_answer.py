def return_n_smallest_chars(str):
    """
            Returns a list of the n smallest characters of a string of distinct characters.
            """
    char_ascii_tuples = [(char, ord(char)) for char in str]
    char_ascii_tuples.sort(key=lambda tup: tup[1])
    return [tup[0] for tup in char_ascii_tuples[:29]]