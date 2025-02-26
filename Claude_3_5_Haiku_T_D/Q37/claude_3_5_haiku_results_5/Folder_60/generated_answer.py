def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 12 <= i <= 77 and ':' <= char <= 'L':
            result.append(char)
    filtered_str = ''.join((c for c in s if c not in result))
    return filtered_str