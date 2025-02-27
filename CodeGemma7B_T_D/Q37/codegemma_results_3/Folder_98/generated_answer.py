def filter_chars(text):
    result = ''
    for i in range(len(text)):
        if i >= 8 and i <= 9 and (text[i] >= 'R') and (text[i] <= 't'):
            continue
        result += text[i]
    return result