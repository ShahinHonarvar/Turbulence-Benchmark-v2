def filter_chars(txt):
    filtered_txt = ''
    for i, char in enumerate(txt):
        if i >= 7 and i <= 9:
            if char >= '6' and char <= 'w':
                continue
        filtered_txt += char
    return filtered_txt