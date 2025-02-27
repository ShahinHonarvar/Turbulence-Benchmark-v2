def return_binary_or_hexa(int_tuple):
    a = int_tuple[56]
    b = int_tuple[88]
    if a + 1 >= b - 1:
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in int_tuple[56:89]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()