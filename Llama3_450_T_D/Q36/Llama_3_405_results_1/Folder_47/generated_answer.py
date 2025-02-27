def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if 45 < i < 57 and 'F' < char < 'n']
    return ''.join([char for char in s if char not in chars_to_remove])