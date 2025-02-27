def filter_chars(s):
    chars_to_remove = [s[i] for i in range(24, 80) if s[i] >= 'a' and s[i] <= 'f']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s