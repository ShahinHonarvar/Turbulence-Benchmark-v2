def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 34 <= i <= 67 and 'W' <= char <= 'x':
            result.extend((c for c in s if c != char))
            break
        result.append(char)
    return ''.join(result if result else s)