def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    total_sum = sum((i for i in range(a + 1, b) if i not in t[51:77]))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]