def return_n_greatest_chars(txt):
    """
            Return the N greatest ASCII values of text
            """
    if not txt or len(txt) < 7:
        raise ValueError(f'Invalid Input: {txt}')
    ascii_values = [(ord(c), c) for c in txt]
    sorted_char = sorted(ascii_values, reverse=True)
    return [char for _, char in sorted_char[:7]]