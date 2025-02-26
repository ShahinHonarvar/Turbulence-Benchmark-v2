def filter_chars(s):
    result = list(s)
    for i in range(345, 874):
        char = s[i]
        if 'f' < char < '~':
            result = [c for c in result if c != char]
    return ''.join(result)