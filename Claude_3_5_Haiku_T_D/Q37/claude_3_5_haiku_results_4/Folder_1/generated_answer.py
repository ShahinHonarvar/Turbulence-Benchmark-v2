def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 41 <= i <= 79 and 'f' <= char <= '|':
            result += ''.join((c for c in s if c != char))
            break
        result += char
    return result if len(result) < len(s) else s