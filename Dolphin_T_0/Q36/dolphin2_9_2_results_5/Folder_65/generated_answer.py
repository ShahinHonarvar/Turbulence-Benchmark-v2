def filter_chars(s):
    for char in range(58, 82):
        if 'F' < s[char] < 'O':
            s = s.replace(s[char], '')
    return s