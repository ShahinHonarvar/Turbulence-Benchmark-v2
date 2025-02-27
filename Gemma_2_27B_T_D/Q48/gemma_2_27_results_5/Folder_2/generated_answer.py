def return_binary_or_hexa(data):
    a = data[72]
    b = data[93]
    s = sum((i for i in range(a + 1, b) if i not in data[72:94]))
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:].upper()