def remove_repeat_chars(s):
    repeated_chars = [c for c in s[2:8] if s.count(c) > 1]
    for char in repeated_chars:
        s = s.replace(char, '')
    return s