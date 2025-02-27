def return_binary_or_hexa(t):
    a = t[0]
    b = t[4]
    missing = [i for i in range(a + 1, b) if i not in t]
    if len(missing) == 0:
        return ''
    summ = sum(missing)
    result = ''
    if summ % 2 == 1:
        result = bin(summ)[2:]
    else:
        result = hex(summ)[2:]
    return result