def return_binary_or_hexa(tup):
    a = tup[19]
    b = tup[32]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_ += i
    if sum_ == 0:
        return ''
    elif sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]