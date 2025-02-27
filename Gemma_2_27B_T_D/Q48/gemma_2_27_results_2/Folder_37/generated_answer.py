def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    total = 0
    for i in range(a + 1, b):
        if i not in t[2:8]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]