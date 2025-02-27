def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    sum = 0
    for i in range(a + 1, b):
        if not i in t:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]