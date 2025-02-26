def filter_chars(input_string):
    filtered_chars = []
    for i, char in enumerate(input_string):
        if i <= 1 and '*' <= char <= 's':
            filtered_chars.extend((c for c in input_string if c != char))
            return ''.join(filtered_chars)
    return input_string