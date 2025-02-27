def return_binary_or_hexa(data):
    a = data[38]
    b = data[81]
    total = sum([i for i in range(a + 1, b) if i not in data[38:81]])
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]