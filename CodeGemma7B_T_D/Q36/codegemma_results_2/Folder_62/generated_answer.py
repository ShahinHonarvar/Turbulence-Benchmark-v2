def filter_chars(txt):
    result = ''
    for i in range(len(txt)):
        if i not in range(64, 90) or txt[i] <= '*' or txt[i] >= 'w':
            result += txt[i]
    return result