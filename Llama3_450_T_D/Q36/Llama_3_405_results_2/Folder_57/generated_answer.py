def filter_chars(s):
    chars_to_remove = [char for char in s[70:74] if 'A' < char < 'U']
    return ''.join([char for char in s if char not in chars_to_remove])