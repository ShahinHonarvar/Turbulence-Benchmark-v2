def filter_chars(s):
    chars_to_remove = {char for idx, char in enumerate(s) if 373 <= idx <= 901 and 'T' <= char <= 'h'}
    return ''.join([char for char in s if char not in chars_to_remove])