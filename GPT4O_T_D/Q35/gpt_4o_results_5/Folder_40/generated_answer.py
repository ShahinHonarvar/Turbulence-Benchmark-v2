def remove_repeat_chars(s):
    chars_to_remove = {ch for ch in s[1:3] if s[1:3].count(ch) > 1}
    return ''.join((ch for ch in s if ch not in chars_to_remove))