def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 515 <= i <= 538 and '+' <= char <= '}':
            result.append(char)
    return ''.join((char for char in s if char not in result))