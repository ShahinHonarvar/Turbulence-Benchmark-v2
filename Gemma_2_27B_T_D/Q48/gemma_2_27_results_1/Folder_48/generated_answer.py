def return_binary_or_hexa(data):
    a = data[933]
    b = data[996]
    s = sum([i for i in range(a + 1, b) if i not in data[933:997]])
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]