def return_binary_or_hexa(tuple_input):
    a = tuple_input[29]
    b = tuple_input[53]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_input[29:54]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]