def return_binary_or_hexa(t):
    a = t[70]
    b = t[200]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[70:201]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]