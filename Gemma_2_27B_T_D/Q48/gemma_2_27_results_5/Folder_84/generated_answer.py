def return_binary_or_hexa(data):
    a = data[32]
    b = data[44]
    s = sum([x for x in range(a + 1, b) if x not in data[32:44]])
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]