def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    total = 0
    for num in range(a + 1, b):
        if num not in t[13:77]:
            total += num
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]