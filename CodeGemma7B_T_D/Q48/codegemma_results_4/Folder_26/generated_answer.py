def return_binary_or_hexa(tuple):
    a = tuple[68]
    b = tuple[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[68:99 + 1]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()