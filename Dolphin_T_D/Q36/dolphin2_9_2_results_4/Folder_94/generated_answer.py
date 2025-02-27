def filter_chars(s):
    new_s = ''
    for char in s:
        if 15 < s.index(char) < 85 and 'I' < char < 'M':
            continue
        new_s += char
    return new_s