def remove_repeat_chars(s):
    start, end = (34, 69)
    sub_s = s[start:end]
    repeat_chars = {c for c in sub_s if sub_s.count(c) > 1}
    result = ''.join((c for c in s if c not in repeat_chars))
    return result