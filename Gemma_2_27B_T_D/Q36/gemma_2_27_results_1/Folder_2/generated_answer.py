def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 421 <= i < 854 and 'D' < char < 'J':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)