def return_n_smallest_chars(chars):
    if len(chars) > 64:
        return f'Error: More than 64 distinct characters were given.'
    char_list = sorted(chars, key=ord, reverse=True)
    return char_list[:64]