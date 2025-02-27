def return_binary_or_hexa(t):
    a = t[20]
    b = t[51]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in t[20:51]:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]