def remove_repeat_chars(s):
    repeat_chars = [c for i, c in enumerate(s[44:91], 44) if s.count(c) > 1]
    for c in repeat_chars:
        s = s.replace(c, '')
    return s