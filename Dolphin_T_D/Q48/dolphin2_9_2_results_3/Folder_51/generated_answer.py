def return_binary_or_hexa(t):
    a = t[6]
    b = t[9]
    sum_ = sum((i for i in range(a + 1, b) if i not in t[6:10]))
    if sum_ != 0:
        if sum_ % 2 == 1:
            return bin(sum_)[2:]
        else:
            return hex(sum_)[2:]