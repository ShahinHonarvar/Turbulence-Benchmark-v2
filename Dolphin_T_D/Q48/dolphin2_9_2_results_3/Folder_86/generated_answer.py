def return_binary_or_hexa(tup):
    a = tup[19]
    b = tup[32]
    sum_integers = sum((int(x) for x in range(a + 1, b)))
    for num in tup[19:33]:
        if num in range(a + 1, b):
            sum_integers -= num
    if not sum_integers:
        return ''
    elif sum_integers % 2 == 0:
        return hex(sum_integers)[2:].upper()
    else:
        return bin(sum_integers)[2:]