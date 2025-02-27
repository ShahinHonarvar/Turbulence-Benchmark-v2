def filter_chars(txt):
    filtered_txt = ''
    for i in range(len(txt)):
        if txt[i] >= 'K' and txt[i] <= 'z' and (i >= 29) and (i <= 79):
            continue
        else:
            filtered_txt += txt[i]
    return filtered_txt