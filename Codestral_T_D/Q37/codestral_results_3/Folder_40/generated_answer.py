def filter_chars(string):
    chars_to_remove = [char for char in string[:2] if '*' <= char <= 's']
    filtered_string = ''.join([char for char in string if char not in chars_to_remove])
    return filtered_string