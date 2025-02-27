def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    sub_str = s[1:7]
    repeat_chars = {c for c in sub_str if sub_str.count(c) > 1}
    result = s[:1] + ''.join((c for c in s[1:] if c not in repeat_chars))
    return result