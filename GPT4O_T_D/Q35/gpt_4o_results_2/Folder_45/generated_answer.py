def remove_repeat_chars(s):
    if not s:
        return s
    sub_string = s[41:200]
    chars_to_remove = {ch for ch in sub_string if sub_string.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in chars_to_remove or s.index(ch) <= 40 or s.index(ch) >= 200))