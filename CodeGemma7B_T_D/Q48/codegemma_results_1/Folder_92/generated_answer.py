def return_binary_or_hexa(var):
    a, b = var
    enum = {i for i in range(a + 1, b)}
    missing = b - (a + 1) - len(enum)
    result = 0
    for i in range(a + 1, b):
        if i not in enum:
            result += i
    return bin(result)[2:] if missing % 2 else hex(result)[2:].upper()