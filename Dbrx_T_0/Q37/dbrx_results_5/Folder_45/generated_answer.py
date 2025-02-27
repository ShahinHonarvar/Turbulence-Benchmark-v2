def filter_chars(s):
    chars_to_remove = ''.join([chr(i) for i in range(ord('.'), ord('b') + 1) if 72 <= i <= 94])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s