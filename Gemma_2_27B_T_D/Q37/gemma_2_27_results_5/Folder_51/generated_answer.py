def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 36 <= i <= 40 and 'H' <= char <= 'e':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)