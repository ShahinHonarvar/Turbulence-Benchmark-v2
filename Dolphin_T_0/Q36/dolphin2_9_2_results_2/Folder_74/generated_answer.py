def filter_chars(input_string):
    chars_to_remove = [c for c in input_string[33:36] if '>' < c < 'A']
    output_string = ''
    for c in input_string:
        if c not in chars_to_remove:
            output_string += c
    return output_string