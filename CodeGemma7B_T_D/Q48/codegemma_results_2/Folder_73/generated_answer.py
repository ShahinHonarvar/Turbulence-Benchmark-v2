def return_binary_or_hexa(tuple_arg):
    a, b = (tuple_arg[10], tuple_arg[76])
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_arg:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()