def filter_chars(text):
    result = ''
    for i in range(len(text)):
        c = text[i]
        if 23 <= i <= 89 and 'w' <= c <= '{':
            result = result.replace(c, '')
        else:
            result += c
    return result