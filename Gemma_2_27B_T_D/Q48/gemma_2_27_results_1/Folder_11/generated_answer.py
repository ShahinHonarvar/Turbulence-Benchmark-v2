def return_binary_or_hexa(t):
    a = t[48]
    b = t[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[48:77]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]