def filter_chars(s):
    chars_to_remove = [s[i] for i in range(2, 7) if s[i] >= '?' and s[i] <= 'f']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s