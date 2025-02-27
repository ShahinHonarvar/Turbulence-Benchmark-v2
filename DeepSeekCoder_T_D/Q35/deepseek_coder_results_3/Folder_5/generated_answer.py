def remove_repeat_chars(s):
    sub_str = s[2:8]
    repeat_chars = {c for c in sub_str if sub_str.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))