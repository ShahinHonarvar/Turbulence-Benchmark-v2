def return_binary_or_hexa(int_tuple):
    a = int_tuple[86]
    b = int_tuple[90]
    sum = 0
    present = set(int_tuple[86:91])
    for i in range(a + 1, b):
        if i not in present:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()