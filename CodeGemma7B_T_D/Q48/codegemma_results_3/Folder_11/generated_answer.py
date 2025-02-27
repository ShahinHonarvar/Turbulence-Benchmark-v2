def return_binary_or_hexa(a, b, t):
    check = 0
    xor = 0
    for i in range(a + 1, b):
        if i not in t[48:76]:
            xor ^= i
            check += 1
    if check % 2 == 1:
        return format(xor, 'b')
    else:
        return format(xor, 'x')