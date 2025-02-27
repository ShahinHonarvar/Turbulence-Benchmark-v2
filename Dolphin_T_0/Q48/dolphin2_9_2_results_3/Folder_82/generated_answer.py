def return_binary_or_hexa(t):
    a = t[20]
    b = t[200]
    s = set(t[21:201])
    sum = 0
    for i in range(a + 1, b):
        if i not in s:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()