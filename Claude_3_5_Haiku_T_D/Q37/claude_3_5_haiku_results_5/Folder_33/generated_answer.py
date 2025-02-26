def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 722 <= i <= 832 and 'K' <= char <= 'm':
            result.append(char)
    return ''.join((char for char in s if char not in result))