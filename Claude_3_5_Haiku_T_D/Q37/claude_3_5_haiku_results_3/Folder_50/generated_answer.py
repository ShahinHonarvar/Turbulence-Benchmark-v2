def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 71 <= i <= 96 and '_' <= char <= 'o':
            s = s.replace(char, '')
    return s