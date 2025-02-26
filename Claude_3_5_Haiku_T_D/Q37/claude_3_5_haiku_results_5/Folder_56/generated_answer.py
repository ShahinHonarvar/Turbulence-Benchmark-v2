def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 71 <= i <= 94 and 'K' <= char <= 'a':
            result.append(char)
    filtered_s = ''.join((char for char in s if char not in result))
    return filtered_s