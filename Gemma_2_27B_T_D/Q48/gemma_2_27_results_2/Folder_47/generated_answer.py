def return_binary_or_hexa(data):
    a = data[29]
    b = data[53]
    total = 0
    for i in range(a + 1, b):
        if i not in data[29:54]:
            total += i
    return bin(total)[2:] if total % 2 else hex(total)[2:]