def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 55 <= i < 84 and ';' < char < 'z':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)