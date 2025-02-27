def remove_repeat_chars(s):
    if len(s) <= 30:
        return s
    sub_str = s[30:53]
    repeated_chars = {c for c in sub_str if sub_str.count(c) > 1}
    result = ''.join((c for c in s if c not in repeated_chars or not 30 < s.index(c) < 53))
    return result