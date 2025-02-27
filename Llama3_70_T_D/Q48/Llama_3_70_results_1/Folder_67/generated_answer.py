def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[67]
    sum_of_integers = sum((i for i in range(a + 1, b) if i not in tup[45:67]))
    if sum_of_integers == 0:
        return ''
    elif sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]