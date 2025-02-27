def return_binary_or_hexa(tuple):
    a = tuple[17]
    b = tuple[88]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[17:89]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()