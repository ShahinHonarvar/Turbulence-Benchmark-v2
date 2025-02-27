def return_binary_or_hexa(tup):
    a, b = (tup[42], tup[87])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[42:87]:
            sum += i
    if sum % 2:
        return format(sum, 'b')
    else:
        return hex(sum).split('x')[-1].upper()