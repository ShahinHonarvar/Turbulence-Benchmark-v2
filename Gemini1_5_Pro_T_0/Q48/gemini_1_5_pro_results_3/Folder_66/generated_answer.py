def return_binary_or_hexa(tuple_input):
    a = tuple_input[11]
    b = tuple_input[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_input[11:77]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]