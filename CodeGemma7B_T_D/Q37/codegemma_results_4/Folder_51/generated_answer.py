def filter_chars(txt):
    result = ''
    for i in range(len(txt)):
        if i >= 36 and i <= 40 and (txt[i] >= 'H') and (txt[i] <= 'e'):
            continue
        result += txt[i]
    return result