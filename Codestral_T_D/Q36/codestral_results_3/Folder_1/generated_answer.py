def filter_chars(s):
    for char in s[69:87]:
        if '#' < char < 'L':
            s = s.replace(char, '')
    return s