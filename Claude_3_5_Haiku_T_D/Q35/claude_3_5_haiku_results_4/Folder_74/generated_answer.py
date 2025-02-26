def remove_repeat_chars(s):
    chars_in_range = s[70:97]
    repeats = set((char for char in chars_in_range if chars_in_range.count(char) > 1))
    return ''.join((char for char in s if char not in repeats or s.index(char) < 70 or s.index(char) >= 97))