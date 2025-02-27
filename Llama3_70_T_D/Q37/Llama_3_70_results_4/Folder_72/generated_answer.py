def filter_chars(s):
    chars_to_remove = set(s[35:51].lower())
    chars_to_remove = {char for char in chars_to_remove if 'h' <= char <= 's'}
    return ''.join((char for char in s if char.lower() not in chars_to_remove))