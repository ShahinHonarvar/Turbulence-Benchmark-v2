def return_binary_or_hexa(t):
    a, b = (t[200], t[202])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[200:203]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()