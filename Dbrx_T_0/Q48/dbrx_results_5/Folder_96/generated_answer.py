def return_binary_or_hexa(t):
    a, b = (t[50], t[200])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[50:201]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()