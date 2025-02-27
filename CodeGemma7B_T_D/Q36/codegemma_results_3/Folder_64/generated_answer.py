def filter_chars(txt):
    for char in range(1, 7):
        if txt[char] > '3' and txt[char] < '^':
            while txt.count(txt[char]):
                txt = txt.replace(txt[char], '', 1)
    return txt