def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    sub_str = s[10:76]
    repeat_chars = {c for c in sub_str if sub_str.count(c) > 1}
    result = s[:10] + ''.join((c for c in s[10:76] if c not in repeat_chars)) + s[76:]
    return result