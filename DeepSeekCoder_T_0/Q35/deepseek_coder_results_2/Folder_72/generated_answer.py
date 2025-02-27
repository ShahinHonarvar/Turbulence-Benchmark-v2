def remove_repeat_chars(s):
    sub_s = s[13:70]
    repeat_chars = {c for c in sub_s if sub_s.count(c) > 1}
    result = ''.join((c for c in s if c not in repeat_chars))
    return result