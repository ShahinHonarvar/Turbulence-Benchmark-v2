def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 344 < i < 874 and 'f' < char < '~':
            result.append(char)
    filtered_string = ''.join(result)
    return filtered_string