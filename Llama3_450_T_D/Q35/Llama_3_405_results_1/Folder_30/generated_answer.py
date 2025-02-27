def remove_repeat_chars(s):
    chars_to_remove = [char for char in set(s[22:24]) if s.count(char) > 1]
    return ''.join([char for char in s if char not in chars_to_remove])