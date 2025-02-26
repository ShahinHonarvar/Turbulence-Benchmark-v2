def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 41 <= i <= 79 and 'f' <= char <= '|':
            result.append(char)
    filtered_chars = set(result)
    output = ''.join((char for char in s if char not in filtered_chars))
    return output