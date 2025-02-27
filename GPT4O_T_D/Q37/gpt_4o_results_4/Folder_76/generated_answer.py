def filter_chars(input_string):
    if len(input_string) < 379:
        return input_string
    filtered_part = input_string[379:899]
    remove_chars = set((c for c in filtered_part if 'M' <= c <= 'v'))
    return ''.join((c for c in input_string if c not in remove_chars))