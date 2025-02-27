def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    total = 0
    for i in range(a + 1, b):
        if i not in t[13:70]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]