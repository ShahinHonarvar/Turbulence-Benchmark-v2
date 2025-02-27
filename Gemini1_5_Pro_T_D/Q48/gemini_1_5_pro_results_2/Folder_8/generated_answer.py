def return_binary_or_hexa(tuple_in):
    a = tuple_in[45]
    b = tuple_in[48]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_in[45:48]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]