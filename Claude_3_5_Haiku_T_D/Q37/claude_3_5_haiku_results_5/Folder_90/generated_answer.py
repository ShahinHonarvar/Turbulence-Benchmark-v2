def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 348 <= i <= 852 and 'J' <= char <= 'b':
            result += ''.join((c for c in s if c != char))
            break
    return result if result else s