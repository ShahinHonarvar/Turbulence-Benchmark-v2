def remove_repeat_chars(s):
    for ch in s[0:3]:
        if s.count(ch) > 1:
            s = ''.join([c for c in s if c != ch])
    return s