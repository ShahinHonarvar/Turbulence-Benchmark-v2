def return_binary_or_hexa(tuple):
    a = tuple[55]
    b = tuple[84]
    sum = 0
    for i in range(a + 1, b):
        if tuple.count(i) == 0:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()