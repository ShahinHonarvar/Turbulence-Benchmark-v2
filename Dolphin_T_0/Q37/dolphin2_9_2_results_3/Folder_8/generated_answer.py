def filter_chars(s):
    for char in range(41, 87):
        if str.encode(s[char]) >= ord('S') and str.encode(s[char]) <= ord('s'):
            s = s.replace(s[char], '')
    return s