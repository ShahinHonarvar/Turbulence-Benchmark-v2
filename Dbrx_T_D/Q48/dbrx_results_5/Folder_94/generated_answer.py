def return_binary_or_hexa(tup):
    a = tup[42]
    b = tup[87]
    sum = 0
    present = set(tup[42:88])
    for i in range(a + 1, b):
        if i not in present:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()