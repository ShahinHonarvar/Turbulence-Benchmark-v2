def insert_after_character(str_input):
    """Inserts 'H' after any occurrences of 'C' in a string."""
    for i in range(len(str_input)):
        if str_input[i] == 'C':
            str_input = str_input[:i + 1] + 'H' + str_input[i + 1:]
    return str_input