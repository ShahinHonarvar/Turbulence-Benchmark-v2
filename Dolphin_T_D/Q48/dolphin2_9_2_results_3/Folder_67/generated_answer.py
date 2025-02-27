def return_binary_or_hexa(t):
    if t[44] > 0:
        a = t[44]
        b = t[67]
        total = 0
        for i in range(a + 1, b):
            if i not in t:
                total += i
        if total % 2 != 0:
            return bin(total)[2:]
        else:
            return hex(total)[2:].upper()
    return ''