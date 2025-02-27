def remove_repeat_chars(s):
    start, end = (38, 52)
    chars_to_remove = {c for c in s if s[start:end].count(c) > 1}
    return ''.join((c for c in s if c not in chars_to_remove))