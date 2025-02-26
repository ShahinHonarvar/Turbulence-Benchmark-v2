def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 41 <= i <= 79 and 'f' <= char <= '|':
            result.append(char)
    new_s = ''.join((char for char in s if char not in result))
    return new_s