def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 171 < i < 636 and 'c' < char < 's':
            result.append(char)
    filtered_result = []
    for char in s:
        if char not in result:
            filtered_result.append(char)
    return ''.join(filtered_result)