def remove_repeat_chars(string):
    chars_to_remove = [c for c in string[33:78] if string.count(c) > 1]
    return ''.join([c for c in string if c not in chars_to_remove])