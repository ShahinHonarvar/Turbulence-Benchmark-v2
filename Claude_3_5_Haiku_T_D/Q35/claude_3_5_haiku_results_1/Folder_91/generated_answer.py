def remove_repeat_chars(s):
    chars = list(s)
    repeated_chars = set((char for char in chars[1:6] if chars[1:6].count(char) > 1))
    return ''.join((char for char in chars if char not in repeated_chars))