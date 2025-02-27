def filter_chars(s):
    result = ''
    for char in s:
        if 138 <= ord(char) <= 920 and '6' <= char <= 'A':
            continue
        result += char
    return result