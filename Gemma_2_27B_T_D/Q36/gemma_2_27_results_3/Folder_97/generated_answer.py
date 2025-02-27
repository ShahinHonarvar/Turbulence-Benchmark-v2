def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 309 or i >= 591:
            result.append(char)
        elif 'S' < char and char < 'm':
            pass
        else:
            result.append(char)
    return ''.join(result)