def return_binary_or_hexa(tup):
    a = tup[77]
    b = tup[84]
    sum_n = sum(list(range(a + 1, b)))
    sum_tuple = sum(tup[77:85])
    if sum_n != sum_tuple:
        if sum_n % 2 == 0:
            return hex(sum_n)[2:]
        else:
            return bin(sum_n)[2:]
    else:
        return ''