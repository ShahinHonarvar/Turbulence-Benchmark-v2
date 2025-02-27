def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 513 <= i <= 877 and '?' <= char <= 'n':
            continue
        result += char
    return result