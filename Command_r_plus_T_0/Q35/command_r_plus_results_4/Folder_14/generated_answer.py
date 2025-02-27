def remove_repeat_chars(s):
    chars_to_remove = [c for c in s[2:5] if s.count(c) > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s