def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 19 <= i <= 32 and 'f' <= char <= 'o':
            result += ''.join((c for c in s if c != char))
            break
        result += char
    return result if len(result) < len(s) else s