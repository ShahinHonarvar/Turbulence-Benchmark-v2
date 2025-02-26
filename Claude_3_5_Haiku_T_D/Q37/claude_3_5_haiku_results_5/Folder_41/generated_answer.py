def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if 26 <= i <= 64 and 'V' <= char <= 'o':
            result += ''.join((c for c in string if c != char))
            break
        result += char
    return result if len(result) < len(string) else string