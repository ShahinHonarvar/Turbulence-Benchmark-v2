def return_binary_or_hexa(data):
    a = data[16]
    b = data[87]
    total = sum((x for x in range(a + 1, b) if x not in data[16:88]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]