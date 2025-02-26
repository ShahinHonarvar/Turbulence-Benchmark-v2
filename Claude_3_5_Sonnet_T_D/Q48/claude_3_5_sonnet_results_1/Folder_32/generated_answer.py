def return_binary_or_hexa(tuple_input):
    a = tuple_input[86]
    b = tuple_input[90]
    sum_value = 0
    for num in range(a + 1, b):
        if num not in tuple_input[86:91]:
            sum_value += num
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].upper()