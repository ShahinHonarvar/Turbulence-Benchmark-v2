def remove_repeat_chars(s):
    repeat_chars = [c for c in s[72:93] if s.count(c) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s