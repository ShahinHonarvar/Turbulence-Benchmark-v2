def return_binary_or_hexa(t):
    a, b = (t[36], t[54])
    present = set(t[36:55])
    sum = 0
    for i in range(a + 1, b):
        if i not in present:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()