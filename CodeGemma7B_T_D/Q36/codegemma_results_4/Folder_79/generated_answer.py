def filter_chars(str):
    out = list(str)
    for i, x in enumerate(out):
        if i in range(11, 46) and x > '!':
            if x not in out or x > out[-1]:
                out.insert(i, x)
    return ''.join(out)