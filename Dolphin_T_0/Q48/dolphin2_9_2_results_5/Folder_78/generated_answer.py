def return_binary_or_hexa(t):
    a = t[62]
    b = t[96]
    sum = 0
    for i in range(a + 1, b):
        if i not in t:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]