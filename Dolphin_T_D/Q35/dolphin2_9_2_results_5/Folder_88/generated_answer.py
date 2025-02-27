def remove_repeat_chars(s):
    chars_to_remove = [c for c in s[3:9] if s.count(c) > 1]
    return ''.join((char for char in s if char not in chars_to_remove))