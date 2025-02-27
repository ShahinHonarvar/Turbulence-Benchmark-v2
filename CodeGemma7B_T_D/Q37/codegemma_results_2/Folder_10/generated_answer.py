def filter_chars(string):
    res = []
    for i in range(len(string)):
        if i >= 63 and i <= 84 and (string[i] >= 'E') and (string[i] <= '~'):
            pass
        else:
            res.append(string[i])
    return ''.join(res)