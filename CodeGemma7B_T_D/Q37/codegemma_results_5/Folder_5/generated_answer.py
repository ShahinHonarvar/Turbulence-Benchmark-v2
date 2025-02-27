def filter_chars(txt):
    start_index = 24
    end_index = 82
    filtered_txt = ''
    for char in txt:
        if char >= '5' and char <= '<' and (txt.index(char) >= start_index) and (txt.index(char) <= end_index):
            continue
        else:
            filtered_txt += char
    return filtered_txt