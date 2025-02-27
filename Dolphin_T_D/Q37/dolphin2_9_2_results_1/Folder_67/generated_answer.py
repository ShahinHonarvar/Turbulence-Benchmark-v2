def filter_chars(s):
    chars = [s[i] for i in range(19, 23) if ']' <= s[i] <= 't']
    for char in chars:
        s = s.replace(char, '')
    return s