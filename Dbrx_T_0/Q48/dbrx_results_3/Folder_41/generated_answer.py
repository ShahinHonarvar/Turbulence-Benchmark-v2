def return_binary_or_hexa(t):
    a, b = (t[3], t[8])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[3:9]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()