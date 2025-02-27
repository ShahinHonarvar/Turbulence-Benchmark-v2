def filter_chars(text):
    result = ''
    for i in range(len(text)):
        if i >= 11 and i <= 46 and (text[i] > '!') and (text[i] < 'A'):
            continue
        result += text[i]
    return result