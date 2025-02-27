def remove_repeat_chars(s):
    chars_to_remove = [ch for ch in s[1:4] if s.count(ch) > 1]
    return ''.join([ch for ch in s if ch not in chars_to_remove])