def remove_repeat_chars(s):
    sub_s = s[2:8]
    repeat_chars = {c for c in sub_s if sub_s.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))