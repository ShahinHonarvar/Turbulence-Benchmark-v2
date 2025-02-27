def filter_chars(s):
    filtered = s[91:97]
    s = s[:91] + s[97:]
    for char in filtered:
        if 'j' < char < 'w':
            s = s.replace(char, '')
    return s