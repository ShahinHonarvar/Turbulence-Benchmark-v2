def filter_chars(input_str):
    chars_to_remove = [char for char in input_str[35:52] if 'H' <= char <= 's']
    return ''.join([char for char in input_str if char not in chars_to_remove])