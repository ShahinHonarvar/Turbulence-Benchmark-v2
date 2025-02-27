def remove_repeat_chars(s):
    repeated_chars = [c for c in s[20:51] if s.count(c) > 1]
    for c in repeated_chars:
        s = ''.join([x for x in s if x != c])
    return s