def return_binary_or_hexa(data):
    a = data[38]
    b = data[81]
    total = sum([x for x in range(a + 1, b) if x not in data[38:82]])
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]