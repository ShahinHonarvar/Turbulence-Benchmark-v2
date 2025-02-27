def return_binary_or_hexa(t):
    a = t[6]
    b = t[7]
    sum = 0
    for n in range(a + 1, b):
        if n not in t[6:8]:
            sum += n
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()