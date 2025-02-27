def remove_repeat_chars(s):
    remove_chars = [c for c in s[46:91] if s.count(c) > 1]
    for char in remove_chars:
        s = s.replace(char, '')
    return s