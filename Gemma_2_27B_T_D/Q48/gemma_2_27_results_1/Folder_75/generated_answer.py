def return_binary_or_hexa(data):
    a = data[20]
    b = data[51]
    total = sum(range(a + 1, b)) - sum([x for x in range(a + 1, b) if x in data[20:51]])
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]