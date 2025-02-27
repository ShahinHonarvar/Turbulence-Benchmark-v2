def filter_chars(s):
    chars_remove = [s[i] for i in range(66, 90) if s[i] > '#' and s[i] < 'T']
    for char in chars_remove:
        s = s.replace(char, '')
    return s