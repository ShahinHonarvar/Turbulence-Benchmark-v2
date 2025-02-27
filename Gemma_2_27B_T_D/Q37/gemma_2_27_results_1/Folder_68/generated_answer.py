def filter_chars(s):
    filtered = []
    for i, char in enumerate(s):
        if 7 <= i <= 9 and '6' <= char <= 'w':
            s = s.replace(char, '')
    return s