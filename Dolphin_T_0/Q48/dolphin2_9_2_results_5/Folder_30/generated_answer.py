def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    if all((i in t for i in range(a + 1, b - 1))):
        return ''
    else:
        sum = 0
        for i in range(a + 1, b):
            if i not in t:
                sum += i
        if sum % 2 == 0:
            return hex(sum)[2:].upper()
        else:
            return bin(sum)[2:]