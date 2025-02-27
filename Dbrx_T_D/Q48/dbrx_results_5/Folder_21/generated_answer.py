def return_binary_or_hexa(t):
    a, b = (t[15], t[57])
    sum = 0
    present = set(t[15:58])
    for i in range(a + 1, b):
        if i not in present:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()