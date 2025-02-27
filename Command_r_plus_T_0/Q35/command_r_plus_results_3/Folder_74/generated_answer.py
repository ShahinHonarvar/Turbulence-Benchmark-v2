def remove_repeat_chars(s):
    repeat_chars = [c for c in s[69:97] if s[69:97].count(c) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s