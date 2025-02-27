def return_binary_or_hexa(tup):
    a = tup[39]
    b = tup[43]
    s = set(tup[40:43])
    total_sum = sum((i for i in range(a + 1, b) if i not in s))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]