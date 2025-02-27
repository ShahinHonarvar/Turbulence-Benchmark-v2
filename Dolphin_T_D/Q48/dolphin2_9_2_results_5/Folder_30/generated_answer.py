def return_binary_or_hexa(arg):
    a = arg[22]
    b = arg[24]
    missing = [i for i in range(a + 1, b) if i not in arg[23:25]]
    if missing:
        summ = sum(missing)
        if summ % 2 == 1:
            return bin(summ)[2:]
        else:
            return hex(summ)[2:]
    else:
        return ''