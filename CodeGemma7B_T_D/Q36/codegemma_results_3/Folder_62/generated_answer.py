def filter_chars(txt):
    filtered_chars = []
    for i in range(len(txt)):
        if i < 63 or i > 88 or txt[i] <= '*' or (txt[i] >= 'w'):
            filtered_chars.append(txt[i])
    return ''.join(filtered_chars)