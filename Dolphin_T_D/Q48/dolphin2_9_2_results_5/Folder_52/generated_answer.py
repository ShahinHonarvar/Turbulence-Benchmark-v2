def return_binary_or_hexa(atuple):
    a = atuple[38]
    b = atuple[81]
    total = 0
    for i in range(a + 1, b):
        if i not in atuple[38:82]:
            total += i
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]