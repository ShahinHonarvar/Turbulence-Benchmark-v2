def return_binary_or_hexa(t):
    a, b = (t[36], t[52])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[36:53]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()