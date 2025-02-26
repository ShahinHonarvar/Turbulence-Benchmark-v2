def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 19 <= i <= 32 and 'f' <= char <= 'o':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string