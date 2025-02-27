def remove_repeat_chars(s):
    if len(s) <= 36:
        return s
    sub_s = s[21:36]
    repeated_chars = {ch for ch in sub_s if sub_s.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in repeated_chars))