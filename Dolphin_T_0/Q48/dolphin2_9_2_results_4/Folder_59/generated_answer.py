def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[1:10]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]