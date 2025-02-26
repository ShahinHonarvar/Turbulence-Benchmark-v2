def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 54 <= i <= 83 and 'j' <= char <= 'v':
            result += ''.join((c for c in s if c != char))
            return result
    return s