def return_binary_or_hexa(tuple):
    a, b = (tuple[39], tuple[43])
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[39:44]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()