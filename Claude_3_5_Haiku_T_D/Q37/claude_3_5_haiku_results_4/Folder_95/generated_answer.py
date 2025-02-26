def filter_chars(s):
    result = list(s)
    for i in range(35, 41):
        if 0 <= i < len(s):
            char = s[i]
            if ')' <= char <= 'l':
                result = [c for c in result if c != char]
    return ''.join(result)