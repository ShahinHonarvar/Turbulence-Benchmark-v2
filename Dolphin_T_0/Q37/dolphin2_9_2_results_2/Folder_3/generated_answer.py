def filter_chars(string):
    chars_to_remove = [string[i] for i in range(37, 57) if string[i] >= '6' and string[i] <= '_']
    return ''.join([char for char in string if char not in chars_to_remove])