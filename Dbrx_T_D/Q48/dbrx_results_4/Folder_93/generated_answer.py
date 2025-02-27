def return_binary_or_hexa(t):
    a, b = (0, 0)
    for i in range(len(t)):
        if i == 57:
            a = t[i]
        elif i == 85:
            b = t[i]
    sum = 0
    for num in range(a + 1, b):
        if num not in t[57:85]:
            sum += num
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()