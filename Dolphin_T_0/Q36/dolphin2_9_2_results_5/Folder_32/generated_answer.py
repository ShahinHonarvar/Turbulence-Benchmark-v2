def filter_chars(s):
    for char in range(40, 63):
        if '7' < s[char] < 'H':
            s = s.replace(s[char], '')
    return s