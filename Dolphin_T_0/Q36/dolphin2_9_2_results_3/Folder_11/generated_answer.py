def filter_chars(s):
    chars_to_remove = [s[i] for i in range(86, 93) if s[i] > 'E' and s[i] < '~']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s