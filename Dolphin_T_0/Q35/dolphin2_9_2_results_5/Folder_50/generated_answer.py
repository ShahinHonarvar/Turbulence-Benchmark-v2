def remove_repeat_chars(s):
    chars_to_remove = {c for c in s[13:76] if s[13:76].count(c) > 1}
    return ''.join((c for c in s if c not in chars_to_remove))