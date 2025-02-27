def filter_chars(nstr):
    dct = {}
    for i in range(309, 591):
        dct[nstr[i]] = dct.get(nstr[i], 0) + 1
    for key in dct:
        if key > 'S' and key < 'm':
            for _ in range(dct[key]):
                nstr = nstr.replace(key, '', 1)
    return nstr