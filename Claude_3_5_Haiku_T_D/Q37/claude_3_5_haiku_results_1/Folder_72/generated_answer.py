def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 35 <= i <= 51 and 'H' <= char <= 's':
            result += ''.join((c for c in s if c != char))
            break
        result += char
    return result if result else s