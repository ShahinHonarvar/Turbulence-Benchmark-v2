def return_binary_or_hexa(int_tuple):
    a = int_tuple[2]
    b = int_tuple[8]
    summ = sum((x for x in range(a + 1, b + 1) if x not in int_tuple[2:9]))
    if summ != 0:
        if summ % 2 == 0:
            return hex(summ)[2:]
        else:
            return bin(summ)[2:]
    else:
        return ''