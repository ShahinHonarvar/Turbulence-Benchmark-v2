def return_binary_or_hexa(idx):
    a, b = (idx[20], idx[93])
    result = 0
    for i in range(a + 1, b):
        if i not in idx:
            result += i
    if result & 1:
        return bin(result)[2:]
    return hex(result)[2:].upper() if result else ''