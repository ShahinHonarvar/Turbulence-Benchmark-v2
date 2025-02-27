def remove_repeat_chars(s):
    chars_to_remove = {ch for ch in s[3:8] if s[3:8].count(ch) > 1}
    return ''.join((ch for ch in s if ch not in chars_to_remove))