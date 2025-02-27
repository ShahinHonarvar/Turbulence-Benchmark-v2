def remove_repeat_chars(s):
    chars_to_remove = [s[i] for i in range(1, 4) if s.count(s[i]) > 1]
    s = ''.join([c for c in s if c not in chars_to_remove])
    return s