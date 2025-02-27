def filter_chars(input_string):
    filtered_chars = [c for c in input_string if c not in input_string[35:41] and c not in range(ord(')'), ord('l') + 1)]
    filtered_string = ''.join(filtered_chars)
    return filtered_string