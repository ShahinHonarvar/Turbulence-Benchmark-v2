def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[37:44]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]