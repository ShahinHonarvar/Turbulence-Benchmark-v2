def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    sum_ = sum((i for i in range(a + 1, b) if i not in t))
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]