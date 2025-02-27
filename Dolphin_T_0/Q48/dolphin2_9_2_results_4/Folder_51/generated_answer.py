def return_binary_or_hexa(tuple):
    a = tuple[6]
    b = tuple[9]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[6:10]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]