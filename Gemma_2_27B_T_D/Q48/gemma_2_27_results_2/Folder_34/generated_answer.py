def return_binary_or_hexa(data):
    a = data[60]
    b = data[200]
    s = sum((i for i in range(a + 1, b) if i not in data[60:201]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]