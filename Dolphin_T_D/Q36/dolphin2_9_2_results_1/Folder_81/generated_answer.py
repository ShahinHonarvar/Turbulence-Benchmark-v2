def filter_chars(s):
    for char in range(51, 76):
        if '5' < s[char] < 'f':
            s = s.replace(s[char], '')
    return s