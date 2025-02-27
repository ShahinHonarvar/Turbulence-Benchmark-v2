def remove_repeat_chars(s):
    if len(s) <= 86:
        return s
    section = s[82:86]
    repeat_chars = {ch for ch in section if section.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in repeat_chars))