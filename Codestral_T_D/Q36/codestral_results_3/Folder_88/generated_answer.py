def filter_chars(s):
    for char in s[78:81]:
        if 'S' < char < '[':
            s = s.replace(char, '')
    return s