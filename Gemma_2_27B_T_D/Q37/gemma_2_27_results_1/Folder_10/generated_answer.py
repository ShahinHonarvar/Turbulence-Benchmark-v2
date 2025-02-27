def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (63 <= i <= 84 and 'E' <= char <= '~'):
            result.append(char)
    return ''.join(result)