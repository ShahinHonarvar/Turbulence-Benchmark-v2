def return_binary_or_hexa(t):
    a, b = (t[73], t[84])
    result = 0
    for i in range(a + 1, b):
        if i not in t[73:85]:
            result += i
    if result & 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper()