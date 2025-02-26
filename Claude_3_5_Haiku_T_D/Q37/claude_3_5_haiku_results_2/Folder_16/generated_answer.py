def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 225 <= i <= 381 and 'D' <= char <= 'Y':
            result.append(char)
    result_str = ''.join(result)
    filtered_str = s.replace(result_str, '')
    return filtered_str