def return_binary_or_hexa(t):
    a = t[60]
    b = t[90]
    sum = 0
    for i in range(a + 1, b):
        if all((i != x for x in t[61:90])):
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    return bin(sum)[2:]