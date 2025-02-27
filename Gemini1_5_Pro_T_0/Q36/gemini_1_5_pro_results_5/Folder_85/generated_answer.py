def filter_chars(text):
    res = ''
    for i in range(len(text)):
        if 55 < i < 80 and 'S' < text[i] < 's':
            continue
        else:
            res += text[i]
    return res