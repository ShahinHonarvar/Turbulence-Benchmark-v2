def filter_chars(input_string):
    result = []
    chars_to_remove = set((c for c in input_string[32:84] if 'm' < c < 'w'))
    for char in input_string:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)