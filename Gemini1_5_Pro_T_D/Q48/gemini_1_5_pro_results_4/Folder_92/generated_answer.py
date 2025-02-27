def return_binary_or_hexa(tuple_input):
    a = tuple_input[0]
    b = tuple_input[2]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_input:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]