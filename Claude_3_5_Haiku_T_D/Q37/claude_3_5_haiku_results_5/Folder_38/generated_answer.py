def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 24 <= i <= 79 and 'a' <= char <= 'f':
            result += ''.join((c for c in s if c != char))
            break
        result += char
    return result if result else s