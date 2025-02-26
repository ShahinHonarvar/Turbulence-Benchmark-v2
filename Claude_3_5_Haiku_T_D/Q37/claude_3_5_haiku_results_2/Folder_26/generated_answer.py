def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 20 <= i <= 62 and 'i' <= char <= 'k':
            result += ''.join((c for c in s if c != char))
            break
        result += char
    return result if result else s