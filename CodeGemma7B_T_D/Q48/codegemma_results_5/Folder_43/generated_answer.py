def return_binary_or_hexa(t):
    a, b = (t[10], t[28])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in t[10:29]:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()