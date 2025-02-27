def return_binary_or_hexa(tup):
    a = tup[90]
    b = tup[97]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[90:98]:
            sum += i
    if sum % 2:
        return format(sum, 'b')
    else:
        return format(sum, '02x')