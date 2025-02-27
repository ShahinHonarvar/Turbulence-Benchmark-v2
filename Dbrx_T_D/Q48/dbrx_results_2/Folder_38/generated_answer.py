def return_binary_or_hexa(tup):
    a, b = (tup[36], tup[85])
    sum = 0
    for num in range(a + 1, b):
        if num not in tup[36:86]:
            sum += num
    if sum % 2 == 1:
        return format(sum, '01b')
    else:
        return format(sum, '01x').upper()