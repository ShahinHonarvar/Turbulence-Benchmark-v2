def remove_repeat_chars(s):
    if len(s) < 99:
        return s
    sub_str = s[70:98]
    repeat_chars = {c for c in sub_str if sub_str.count(c) > 1}
    result = ''.join((c for c in s if c not in repeat_chars))
    return result