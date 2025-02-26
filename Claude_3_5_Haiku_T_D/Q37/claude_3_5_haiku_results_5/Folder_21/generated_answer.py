def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 603 <= i <= 759 and 'Q' <= char <= 'h':
            result.append(char)
    return ''.join((char for char in s if char not in result))