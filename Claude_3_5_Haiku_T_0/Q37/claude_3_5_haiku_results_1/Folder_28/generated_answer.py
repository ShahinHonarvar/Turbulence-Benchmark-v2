def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 20 <= i <= 79 and '!' <= char <= 'T':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string