def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[35]
    result = 0
    for i in range(a + 1, b):
        if i not in tup[20:36]:
            result += i
    return str(bin(result))[2:] if result % 2 != 0 else str(hex(result))[2:].upper()