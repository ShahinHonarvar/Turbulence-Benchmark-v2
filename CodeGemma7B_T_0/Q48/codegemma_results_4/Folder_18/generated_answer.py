def return_binary_or_hexa(tu):
    a = tu[56]
    b = tu[90]
    sum = 0
    for i in range(a + 1, b):
        if i not in tu[56:91]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()