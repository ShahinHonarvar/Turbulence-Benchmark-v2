def return_binary_or_hexa(tuple_input):
    a = tuple_input[13]
    b = tuple_input[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_input[13:77]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]