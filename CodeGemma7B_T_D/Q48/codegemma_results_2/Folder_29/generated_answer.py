def return_binary_or_hexa(tup):
    a = tup[70]
    b = tup[98]
    sum = 0
    for i in range(a + 1, b):
        if tup[i] not in tup[70:99]:
            sum += tup[i]
    if sum % 2 == 1:
        return format(sum, 'b')
    else:
        return format(sum, 'x')