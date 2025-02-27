def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    sub = s[1:3]
    repeat_chars = {c for c in sub if sub.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))