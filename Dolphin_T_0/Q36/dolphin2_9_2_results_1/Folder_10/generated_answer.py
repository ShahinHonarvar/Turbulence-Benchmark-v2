def filter_chars(s):
    chars_to_filter = [s[i] for i in range(35, 60) if s[i] > '!' and s[i] < 'B']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s