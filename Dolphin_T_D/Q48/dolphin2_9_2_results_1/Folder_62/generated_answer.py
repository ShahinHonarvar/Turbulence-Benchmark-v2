def return_binary_or_hexa(t):
    a = t[50]
    b = t[92] + 1
    s = set(range(a + 1, b)) - set(t[50:93])
    sum_ = sum(s)
    if sum_ % 2 == 0:
        return hex(sum_)[2:]
    else:
        return bin(sum_)[2:]