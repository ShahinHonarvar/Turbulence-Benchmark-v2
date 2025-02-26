def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 35 <= i <= 98 and 'A' <= char <= 'b':
            result += ''.join((c for c in s if c != char))
            break
    return result if result else s