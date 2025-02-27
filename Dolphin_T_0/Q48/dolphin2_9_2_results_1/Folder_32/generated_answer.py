def return_binary_or_hexa(num_tuple):
    a = num_tuple[86]
    b = num_tuple[90]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in num_tuple[86:91]:
            sum_ += i
    if sum_ % 2 != 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()