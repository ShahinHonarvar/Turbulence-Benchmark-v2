def remove_repeat_chars(string):
    chars_to_remove = set([c for c in string[33:78] if string[33:78].count(c) > 1])
    return ''.join([c for c in string if c not in chars_to_remove])