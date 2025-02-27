def filter_chars(txt):
    result = ''
    for i in range(len(txt)):
        if i >= 32 and i <= 46 and (txt[i] >= '0') and (txt[i] <= 'k'):
            continue
        result += txt[i]
    return result