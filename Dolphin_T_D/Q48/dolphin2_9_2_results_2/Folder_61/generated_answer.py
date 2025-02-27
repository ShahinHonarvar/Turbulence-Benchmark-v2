def return_binary_or_hexa(t):
    sum_ = 0
    a, b = (t[0], t[8])
    for i in range(a + 1, b):
        if i not in t:
            sum_ += i
    if sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]