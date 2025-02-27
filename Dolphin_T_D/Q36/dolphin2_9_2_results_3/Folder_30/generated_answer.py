def filter_chars(s):
    for char in range(23, 45):
        if '3' < s[char] < 'I':
            s = s.replace(s[char], '')
    return s