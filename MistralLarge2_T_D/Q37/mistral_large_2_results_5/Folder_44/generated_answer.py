def filter_chars(s):
    chars_to_remove = set(s[21:44]) & set('+012345678')
    return ''.join([char for char in s if char not in chars_to_remove])