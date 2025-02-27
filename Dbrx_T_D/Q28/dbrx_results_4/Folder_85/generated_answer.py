def return_nth_smallest_ascii(input_string):
    if len(input_string) < 86:
        raise IndexError('Input string too short')
    sorted_chars = sorted(input_string[17:87])
    if len(sorted_chars) < 15:
        raise IndexError('Not enough distinct characters')
    return sorted_chars[14]