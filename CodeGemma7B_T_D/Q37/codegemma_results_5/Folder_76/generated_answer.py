def filter_chars(string):
    for i in range(379, 899):
        if string[i] in 'MVaAbBcCDdDeEfFGgHhiIjklLmMnNoOpPqQRrSsTtUuVvWwXxYyZz':
            string = string[:i] + string[i + 1:]
    return string