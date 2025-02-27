def return_binary_or_hexa(tuple: tuple):
    a, b = (tuple[34], tuple[69])
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[34:69]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()