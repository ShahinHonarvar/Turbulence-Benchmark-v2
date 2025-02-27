def return_binary_or_hexa(n):
    a, b = (n[20], n[43])
    result = sum((i for i in range(a + 1, b) if i not in n[20:44]))
    return bin(result)[2:] if result % 2 else hex(result)[2:].lower() if result % 2 else ''