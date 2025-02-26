def remove_repeat_chars(s):
    if len(s) <= 6:
        return s
    chars_in_range = s[1:5]
    repeats = set((char for char in chars_in_range if chars_in_range.count(char) > 1))
    return ''.join((char for char in s if char not in repeats))