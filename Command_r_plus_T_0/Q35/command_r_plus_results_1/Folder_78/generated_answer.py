def remove_repeat_chars(s):
    repeat_chars = [c for c in s[62:96] if s[62:96].count(c) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s