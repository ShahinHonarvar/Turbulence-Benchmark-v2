def return_binary_or_hexa(t):
    a, b = (t[11], t[76])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[11:77]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()