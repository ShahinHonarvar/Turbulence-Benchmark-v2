def filter_chars(strg):
    new_strg = ''
    for i in range(len(strg)):
        if i in range(384, 412):
            if strg[i] >= '/' and strg[i] <= '8':
                continue
        new_strg += strg[i]
    return new_strg