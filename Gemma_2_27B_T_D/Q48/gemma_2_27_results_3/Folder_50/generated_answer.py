def return_binary_or_hexa(data):
    a = data[13]
    b = data[76]
    s = sum((i for i in range(a + 1, b) if i not in data[13:77]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]