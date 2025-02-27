def return_binary_or_hexa(data):
    a = data[29]
    b = data[53]
    total = 0
    for i in range(a + 1, b):
        if i not in data[29:53]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()