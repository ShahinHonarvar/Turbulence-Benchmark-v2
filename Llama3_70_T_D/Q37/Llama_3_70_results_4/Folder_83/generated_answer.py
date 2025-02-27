def filter_chars(s):
    count = 0
    for char in s:
        count += 1
        if 29 <= count <= 79 and 'K' <= char <= 'z':
            s = s.replace(char, '')
    return s