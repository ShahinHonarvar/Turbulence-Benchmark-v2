def filter_chars(s):
    chars_to_remove = [s[i] for i in range(3, 8) if s[i] > '?' and s[i] < 'k']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s