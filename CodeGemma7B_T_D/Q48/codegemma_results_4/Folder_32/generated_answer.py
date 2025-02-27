def return_binary_or_hexa(tup):
    summ = 0
    for k in range(tup[86] + 1, tup[90]):
        if k not in tup[86:91]:
            summ += k
    if summ % 2 == 0:
        return '%x' % summ if summ >= 16 else str(summ)
    else:
        return bin(summ)[2:]