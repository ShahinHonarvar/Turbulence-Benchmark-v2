def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 669 <= i < 888 and 'B' < char < 'Y':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)