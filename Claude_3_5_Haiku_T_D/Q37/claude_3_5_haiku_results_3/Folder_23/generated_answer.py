def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 51 <= i <= 77 and 'V' <= char <= 'Y':
            result.append(char)
    filtered_string = ''.join((c for c in s if c not in result))
    return filtered_string