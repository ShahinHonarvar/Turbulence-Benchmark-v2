def return_binary_or_hexa(integers):
    a = integers[20]
    b = integers[51]
    missing_integers = [i for i in range(a + 1, b) if i not in integers[21:51]]
    sum_missing_integers = sum(missing_integers)
    if all((i in integers[21:51] for i in range(a + 1, b))):
        return ''
    elif sum_missing_integers % 2 == 0:
        return hex(sum_missing_integers)[2:]
    else:
        return bin(sum_missing_integers)[2:]