def return_binary_or_hexa(tuple_in):
    a = tuple_in[17]
    b = tuple_in[88]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_in[17:88]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 0:
        return hex(sum)[2:].lstrip('0')
    else:
        return bin(sum)[2:].lstrip('0')