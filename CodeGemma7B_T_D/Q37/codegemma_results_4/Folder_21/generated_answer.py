def filter_chars(txt):
    result = ''
    for i in range(len(txt)):
        if i >= 603 and i <= 759 and (txt[i] >= 'Q') and (txt[i] <= 'h'):
            continue
        result += txt[i]
    return result