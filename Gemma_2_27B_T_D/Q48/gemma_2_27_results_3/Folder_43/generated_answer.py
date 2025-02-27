def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[10:28]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()