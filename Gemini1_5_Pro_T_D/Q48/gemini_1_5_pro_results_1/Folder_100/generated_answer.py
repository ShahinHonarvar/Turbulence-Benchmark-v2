def return_binary_or_hexa(tuple_in):
    a = tuple_in[44]
    b = tuple_in[78]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_in[44:78]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]