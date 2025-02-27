def return_binary_or_hexa(data):
    a = data[77]
    b = data[84]
    total = sum([i for i in range(a + 1, b) if i not in data[77:85]])
    return bin(total)[2:] if total % 2 else hex(total)[2:].upper()