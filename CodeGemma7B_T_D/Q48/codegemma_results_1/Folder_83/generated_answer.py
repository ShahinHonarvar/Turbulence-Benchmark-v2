def return_binary_or_hexa(tup):
    a, b = (tup[90], tup[200])
    result = 0
    for i in range(a + 1, b):
        if not i in tup[90:201]:
            result += i
    if result % 2 == 1:
        return str(bin(result))[2:]
    else:
        return hex(result)[2:].upper()