def return_binary_or_hexa(t):
    if 19 < len(t) and 32 < len(t):
        a = t[19]
        b = t[32]
        sum = 0
        for i in range(a + 1, b, 1):
            if i not in t:
                sum += i
        if sum % 2 != 0:
            return bin(sum)[2:]
        else:
            return hex(sum)[2:]
    return ''