def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 373 <= i <= 901 and 'T' <= char <= 'h':
            result += ''.join((c for c in s if c != char))
            break
        result += char
    return result if len(result) < len(s) else s