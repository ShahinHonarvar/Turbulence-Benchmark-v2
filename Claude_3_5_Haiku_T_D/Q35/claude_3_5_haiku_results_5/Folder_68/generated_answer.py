def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    chars_in_range = s[1:9]
    repeat_chars = set((char for char in chars_in_range if chars_in_range.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars))
    return result