def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[56:90]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]