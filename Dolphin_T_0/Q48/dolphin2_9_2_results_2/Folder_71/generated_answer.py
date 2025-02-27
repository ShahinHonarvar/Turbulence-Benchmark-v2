def return_binary_or_hexa(t):
    a, b = (t[20], t[35])
    if all((i in t[21:35] for i in range(a + 1, b))):
        return ''
    else:
        summ = sum((i for i in range(a + 1, b) if i not in t[21:35]))
        if summ % 2:
            return bin(summ)[2:]
        else:
            return hex(summ)[2:]