def filter_chars(txt):
    output_txt = ''
    for i in range(len(txt)):
        if i >= 24 and i <= 82 and (txt[i] >= '5') and (txt[i] <= '<'):
            continue
        else:
            output_txt += txt[i]
    return output_txt