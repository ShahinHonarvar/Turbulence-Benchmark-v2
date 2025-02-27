def return_binary_or_hexa(t):
    a = t[10]
    b = t[79]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[10:80]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]