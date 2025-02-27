def filter_chars(s):
    res = []
    for i, char in enumerate(s):
        if i < 41 or i > 64 or char < 'K' or (char > ']'):
            res.append(char)
    return ''.join(res)