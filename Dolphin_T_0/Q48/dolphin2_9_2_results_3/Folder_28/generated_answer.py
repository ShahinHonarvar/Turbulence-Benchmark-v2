def return_binary_or_hexa(t):
    a = t[86]
    b = t[99]
    sum_ = sum(set(range(a + 1, b)) - set(t[87:99]))
    if sum_ % 2 == 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]