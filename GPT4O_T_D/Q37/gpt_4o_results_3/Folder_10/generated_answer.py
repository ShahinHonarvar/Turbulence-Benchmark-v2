def filter_chars(input_string):
    if len(input_string) <= 84:
        part_to_check = input_string[63:]
    else:
        part_to_check = input_string[63:85]
    chars_to_remove = set((c for c in part_to_check if 'E' <= c <= '~'))
    return ''.join((c for c in input_string if c not in chars_to_remove))