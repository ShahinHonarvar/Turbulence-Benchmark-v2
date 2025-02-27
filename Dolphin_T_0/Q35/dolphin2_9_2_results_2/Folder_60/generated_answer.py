def remove_repeat_chars(s):
    for c in set(s[38:52]):
        if s[38:52].count(c) > 1:
            s = ''.join((d for d in s if d != c))
    return s