def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i > 32 and i < 61 and ('3' < char < 'D'):
            continue
        result.append(char)
    return ''.join(result)