def return_binary_or_hexa(t):
    a, b = (t[0], t[10])
    if a + 1 > b:
        return ''
    sum_ = 0
    for i in range(a + 1, b):
        if i not in t:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]