def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 46 <= i <= 85 and '-' <= char <= 'X':
            result += ''.join((c for c in s if c != char))
            break
        else:
            result += char
    return result if result else s