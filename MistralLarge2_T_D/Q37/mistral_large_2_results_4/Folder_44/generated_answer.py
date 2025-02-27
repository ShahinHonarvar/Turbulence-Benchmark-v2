def filter_chars(s):
    chars_to_remove = {char for i, char in enumerate(s) if 21 <= i <= 43 and '+' <= char <= '8'}
    return ''.join((char for char in s if char not in chars_to_remove))