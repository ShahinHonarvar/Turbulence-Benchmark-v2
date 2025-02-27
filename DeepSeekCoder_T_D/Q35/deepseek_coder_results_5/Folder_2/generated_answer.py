def remove_repeat_chars(s):
    start, end = (72, 93)
    if start < len(s) and end < len(s):
        sub_s = s[start:end]
        repeat_chars = {c for c in sub_s if sub_s.count(c) > 1}
        result = ''.join((c for c in s if c not in repeat_chars))
    else:
        result = s
    return result