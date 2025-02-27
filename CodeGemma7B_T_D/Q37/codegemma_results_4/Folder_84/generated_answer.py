def filter_chars(txt):
    output = ''
    for i in range(len(txt)):
        if i >= 138 and i <= 920 and (txt[i] >= '6') and (txt[i] <= 'A'):
            continue
        output += txt[i]
    return output