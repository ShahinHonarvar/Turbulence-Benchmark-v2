def return_binary_or_hexa(t):
    a, b = (t[43], t[70])
    result = 0
    for i in range(a + 1, b):
        if i not in t[43:71]:
            result += i
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper()