def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i <= 32 or i >= 84 or (not 'm' < char < 'w'):
            result.append(char)
    return ''.join(result)