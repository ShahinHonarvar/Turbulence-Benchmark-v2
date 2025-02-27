def remove_repeat_chars(s):
    chars = [s[i] for i in range(5) if s.count(s[i]) > 1]
    for char in chars:
        s = ''.join([c for c in s if c != char])
    return s