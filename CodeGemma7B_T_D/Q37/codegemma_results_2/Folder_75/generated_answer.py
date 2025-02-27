def filter_chars(GivenString):
    rtn = GivenString
    for i in range(34, 67 + 1):
        rtn = rtn.replace(rtn[i], '')
    return rtn