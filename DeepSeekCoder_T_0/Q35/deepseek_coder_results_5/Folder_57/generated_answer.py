def remove_repeat_chars(s):
    start, end = (25, 80)
    if start < len(s):
        sub_s = s[start:end]
        repeat_chars = {c for c in sub_s if sub_s.count(c) > 1}
        s = ''.join((c for c in s if c not in repeat_chars))
    return s