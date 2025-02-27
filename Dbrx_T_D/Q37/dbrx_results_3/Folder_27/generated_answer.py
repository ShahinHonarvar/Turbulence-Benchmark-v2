def filter_chars(input_string):
    chars_to_keep = set(range(ord('='), ord('E') + 1))
    filtered_chars = [char for char in input_string if char not in chars_to_keep]
    return ''.join(filtered_chars)