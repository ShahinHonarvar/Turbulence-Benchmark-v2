def remove_repeat_chars(s):
    chars_to_remove = [s[i] for i in range(476, 709) if s.count(s[i]) > 1]
    return ''.join([c for c in s if c not in chars_to_remove])