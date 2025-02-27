def return_binary_or_hexa(n):
    a, b = (n[20], n[35])
    result = 0
    for i in range(a + 1, b):
        if i not in n[20:36]:
            result += i
    return str(bin(result))[2:] if result % 2 else hex(result)[2:].upper()