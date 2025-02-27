def return_binary_or_hexa(t):
    a = t[90]
    b = t[97]
    sum = 0
    for i in range(a + 1, b):
        if i not in t:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()
    return ''