def remove_repeat_chars(s):
    repeated_chars = [c for c in s[56:90] if s[56:90].count(c) > 1]
    for char in repeated_chars:
        s = s.replace(char, '')
    return s