def return_binary_or_hexa(tuple_):
    a, b = (tuple_[68], tuple_[99])
    sum_ = 0
    for i in range(a + 1, b):
        if not i in tuple_[68:99]:
            sum_ += i
    if sum_ % 2 != 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()