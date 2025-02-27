def remove_repeat_chars(s):
    chars_to_remove = {ch for ch in s[11:76] if s[11:76].count(ch) > 1}
    return ''.join((ch for ch in s if ch not in chars_to_remove))