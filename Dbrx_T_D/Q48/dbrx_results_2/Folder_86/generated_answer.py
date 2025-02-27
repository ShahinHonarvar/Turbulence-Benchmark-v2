def return_binary_or_hexa(arg_tuple):
    a = arg_tuple[19]
    b = arg_tuple[32]
    sum = 0
    for i in range(a + 1, b):
        if i not in arg_tuple[19:33]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()