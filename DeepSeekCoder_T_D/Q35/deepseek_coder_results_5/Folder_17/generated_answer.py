def remove_repeat_chars(s):
    start, end = (73, 84)
    if start < len(s) and end < len(s):
        sub_str = s[start:end]
        repeat_chars = {c for c in sub_str if sub_str.count(c) > 1}
        result = ''.join((c for c in s if c not in repeat_chars))
    else:
        result = s
    return result