def return_binary_or_hexa(t):
    a, b = (t[40], t[200])
    sum = 0
    for i in range(a + 1, b):
        if not i in t[40:201]:
            sum += i
    if sum & 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper() if sum > 15 else hex(sum)[2:]