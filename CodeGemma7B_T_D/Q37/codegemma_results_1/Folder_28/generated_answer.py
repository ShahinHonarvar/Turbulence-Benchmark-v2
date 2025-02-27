def filter_chars(txt):
    filtered_txt = []
    for i, c in enumerate(txt):
        if not (20 <= i <= 79 and c.isalpha() and (c in ['!', 'T']) and (c not in filtered_txt)):
            filtered_txt.append(c)
    return ''.join(filtered_txt)