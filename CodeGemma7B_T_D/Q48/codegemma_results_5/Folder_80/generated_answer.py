def return_binary_or_hexa(t):
    a, b = (t[57], t[84])
    sum_range = sum((n for n in range(a + 1, b) if n not in t[57:85]))
    if sum_range % 2:
        return bin(sum_range)[2:]
    return hex(sum_range)[2:].upper()