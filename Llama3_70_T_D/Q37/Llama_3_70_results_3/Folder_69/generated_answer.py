def filter_chars(s):
    chars_to_remove = set(s[114:639] if len(s) > 639 else s[114:])
    chars_to_remove = {char for char in chars_to_remove if '!' <= char <= 'x'}
    return ''.join([char for char in s if char not in chars_to_remove])