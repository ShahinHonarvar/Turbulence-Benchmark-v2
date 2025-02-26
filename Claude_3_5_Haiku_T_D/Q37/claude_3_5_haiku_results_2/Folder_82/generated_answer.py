def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 12 <= i <= 25 and 'P' <= char <= 'x':
            filtered_chars.append(char)
    result = ''.join((char for char in s if char not in filtered_chars))
    return result