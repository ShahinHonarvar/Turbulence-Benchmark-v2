def remove_repeat_chars(s):
    if len(s) <= 36:
        return s
    start, end = (37, 54)
    sub_str = s[start:end]
    repeat_chars = {ch for ch in sub_str if sub_str.count(ch) > 1}
    result = ''.join((ch for ch in s if ch not in repeat_chars))
    return result