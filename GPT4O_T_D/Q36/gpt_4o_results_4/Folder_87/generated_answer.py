def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i <= 32 or i >= 61 or (not '3' < char < 'D'):
            result.append(char)
    return ''.join(result)