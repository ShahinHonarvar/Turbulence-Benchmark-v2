def filter_chars(string):
    chars_to_remove = [char for char in string[221:419] if '-' < char < 'v']
    filtered_string = ''.join([char for char in string if char not in chars_to_remove])
    return filtered_string