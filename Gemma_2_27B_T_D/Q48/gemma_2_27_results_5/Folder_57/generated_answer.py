def return_binary_or_hexa(data):
    a = data[25]
    b = data[80]
    total = sum(range(a + 1, b))
    for i in range(25, 80):
        total -= data[i]
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]