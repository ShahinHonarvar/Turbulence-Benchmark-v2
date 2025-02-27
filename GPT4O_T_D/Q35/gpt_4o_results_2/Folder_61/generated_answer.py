def remove_repeat_chars(s):
    substring = s[1:8]
    chars_to_remove = {ch for ch in substring if substring.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in chars_to_remove))