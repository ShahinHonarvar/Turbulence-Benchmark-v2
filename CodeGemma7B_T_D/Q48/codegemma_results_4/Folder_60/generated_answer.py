def return_binary_or_hexa(tup):
    result = 0
    a, b = (tup[38], tup[52])
    for i in range(a + 1, b):
        if i not in tup[38:53]:
            result += i
    if result % 2:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper() if result else ''