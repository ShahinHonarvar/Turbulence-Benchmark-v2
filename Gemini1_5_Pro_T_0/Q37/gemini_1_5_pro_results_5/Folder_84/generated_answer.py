def filter_chars(s):
    new_s = ''
    for i, char in enumerate(s):
        if 138 <= i <= 920 and '6' <= char <= 'A':
            new_s += s.replace(char, '')
            break
        else:
            new_s += char
    return new_s