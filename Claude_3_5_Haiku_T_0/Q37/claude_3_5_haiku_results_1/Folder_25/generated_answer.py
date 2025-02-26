def filter_chars(s):
    result = list(s)
    for i in range(31, 39):
        if 0 <= i < len(s):
            char = s[i]
            if ';' <= char <= 'g':
                result = [c for c in result if c != char]
    return ''.join(result)