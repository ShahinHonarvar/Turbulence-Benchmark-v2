def filter_chars(s):
    result = list(s)
    for i in range(603, 760):
        if i < len(s):
            char = s[i]
            if 'Q' <= char <= 'h':
                result = [c for c in result if c != char]
    return ''.join(result)