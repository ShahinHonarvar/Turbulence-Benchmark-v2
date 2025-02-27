def filter_chars(s):
    chars_to_remove = [char for char in s[318:337] if 'B' < char < 'z']
    return ''.join([char for char in s if char not in chars_to_remove])