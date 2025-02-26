def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 722 <= i <= 832 and 'K' <= char <= 'm':
            result.append(char)
    filtered_string = ''.join((c for c in s if c not in result))
    return filtered_string