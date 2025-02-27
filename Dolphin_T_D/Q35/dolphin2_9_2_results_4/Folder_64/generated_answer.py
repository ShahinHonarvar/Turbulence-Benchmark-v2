def remove_repeat_chars(s):
    chars_to_remove = [c for c in s[:6] if s.count(c) > 1]
    new_s = ''.join([c for c in s if c not in chars_to_remove])
    return new_s