def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if 81 < i < 86 and '!' < char < 's']
    return ''.join([char for char in s if char not in chars_to_remove])