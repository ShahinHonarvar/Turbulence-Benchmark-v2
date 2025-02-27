def return_binary_or_hexa(t):
    a = t[42]
    b = t[87]
    sum_ = sum((x for x in range(a + 1, b) if x not in t[42:88]))
    if sum_ % 2 == 0:
        return hex(sum_)[2:]
    else:
        return bin(sum_)[2:]