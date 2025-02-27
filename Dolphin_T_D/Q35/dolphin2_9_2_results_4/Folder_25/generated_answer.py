def remove_repeat_chars(s):
    chars_to_remove = [ch for ch in s[37:43] if s.count(ch) > 1]
    return ''.join([ch for ch in s if ch not in chars_to_remove])