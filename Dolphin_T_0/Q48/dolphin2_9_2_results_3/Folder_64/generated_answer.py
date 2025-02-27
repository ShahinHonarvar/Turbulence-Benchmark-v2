def return_binary_or_hexa(t):
    a = t[0]
    b = t[5]
    total = 0
    for i in range(a + 1, b):
        total += i
        if i in t:
            total -= i
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]