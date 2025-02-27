def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[33:79]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()