def remove_repeat_chars(s):
    s = s[:90] + s[200:]
    repeated_chars = [c for c in s if s.count(c) > 1]
    for c in repeated_chars:
        s = s.replace(c, '')
    return s