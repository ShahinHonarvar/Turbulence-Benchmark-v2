def return_binary_or_hexa(tuple_in):
    a = tuple_in[22]
    b = tuple_in[24]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_in[22:24]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]