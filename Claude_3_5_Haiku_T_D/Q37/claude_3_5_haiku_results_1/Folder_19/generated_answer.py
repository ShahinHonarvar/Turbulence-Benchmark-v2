def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 35 <= i <= 89 and 'E' <= char <= 't':
            result += s.replace(char, '')
            break
        result += char
    return result