def return_binary_or_hexa(t):
    a, b = (t[0], t[2])
    sum = 0
    for i in range(a + 1, b):
        if i not in t:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]