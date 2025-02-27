def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if 63 < i < 89 and '*' < char < 'w']
    return ''.join([char for char in s if char not in chars_to_remove])