def remove_repeat_chars(s):
    if len(s) <= 92:
        return s
    sub_str = s[50:92]
    repeat_chars = {c for c in sub_str if sub_str.count(c) > 1}
    result = ''.join((c for c in s if c not in repeat_chars))
    return result