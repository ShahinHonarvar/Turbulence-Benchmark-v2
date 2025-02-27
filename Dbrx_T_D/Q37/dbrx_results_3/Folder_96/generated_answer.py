def filter_chars(input_string):
    target_indices = range(86, 93)
    target_ascii = range(ord('!'), ord('s') + 1)
    result = []
    for i, char in enumerate(input_string):
        if i in target_indices and ord(char) in target_ascii:
            continue
        result.append(char)
    return ''.join(result)