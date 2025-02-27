def return_binary_or_hexa(tuple):
    a, b = (tuple[10], tuple[76])
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[10:76]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()