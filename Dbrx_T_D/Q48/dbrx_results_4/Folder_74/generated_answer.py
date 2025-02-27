def return_binary_or_hexa(tup):
    a = tup[69]
    b = tup[97]
    sum = 0
    present = set(tup[70:97])
    for i in range(a + 1, b):
        if i not in present:
            sum += i
    if sum % 2 != 0:
        return format(sum, 'b')
    else:
        return format(sum, 'x')