def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    sum_numbers = sum((x for x in range(a + 1, b) if x not in t[57:85]))
    if sum_numbers % 2 != 0:
        return bin(sum_numbers)[2:]
    else:
        return hex(sum_numbers)[2:]