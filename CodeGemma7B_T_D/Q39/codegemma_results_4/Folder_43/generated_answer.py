def return_n_greatest_chars(str):
    """
            This function takes a string of distinct characters and creates the sorted list of exactly 56 characters of the given string that have
            the greatest ASCII values. The function sorts the list in descending order and returns it.
            """
    ascii_values = {}
    for char in str:
        ascii_values[char] = ord(char)
    char_ascii_tuples = [(char, ascii_values[char]) for char in ascii_values]
    char_ascii_tuples.sort(key=lambda tuple: tuple[1], reverse=True)
    greatest_chars = [tup[0] for tup in char_ascii_tuples[:56]]
    return greatest_chars