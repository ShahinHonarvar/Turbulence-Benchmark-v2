def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 69 <= i < 97 and 'V' < char < 'j':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)