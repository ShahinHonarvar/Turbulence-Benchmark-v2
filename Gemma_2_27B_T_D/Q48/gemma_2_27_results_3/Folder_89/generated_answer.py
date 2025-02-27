def return_binary_or_hexa(data):
    a = data[55]
    b = data[84]
    total = sum([x for x in range(a + 1, b) if x not in data[55:84]])
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]