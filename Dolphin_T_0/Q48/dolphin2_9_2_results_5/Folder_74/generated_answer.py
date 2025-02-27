def return_binary_or_hexa(t):
    a = t[69]
    b = t[97]
    missing = [i for i in range(a + 1, b) if i not in t[69:98]]
    summ = sum(missing)
    res = ''
    if summ % 2 != 0:
        res = bin(summ)[2:]
    else:
        res = hex(summ)[2:]
    if missing == list(range(a + 1, b)):
        return res
    else:
        return ''