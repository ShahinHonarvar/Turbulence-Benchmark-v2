def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 283 <= i < 484 and 'l' < char < 't':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)