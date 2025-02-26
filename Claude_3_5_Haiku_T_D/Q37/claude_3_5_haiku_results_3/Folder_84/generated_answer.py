def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 138 <= i <= 920 and '6' <= char <= 'A':
            result += ''.join((c for c in s if c != char))
            break
        result += char
    return result