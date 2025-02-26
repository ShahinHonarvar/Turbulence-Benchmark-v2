def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 17 <= i <= 63 and 'O' <= char <= '^':
            result.append(char)
    filtered_string = ''.join((c for c in s if c not in result))
    return filtered_string