def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 63 <= i <= 84 and 'E' <= char <= '~':
            result.append(char)
    filtered_string = ''.join((c for c in s if c not in result))
    return filtered_string