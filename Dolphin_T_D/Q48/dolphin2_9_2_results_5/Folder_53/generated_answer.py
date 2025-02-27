def return_binary_or_hexa(tuple_):
    a = tuple_[200]
    b = tuple_[202]
    if a + 1 > b:
        return ''
    sum_ = sum((i for i in range(a + 1, b) if i not in tuple_[200:203]))
    if sum_ % 2 == 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]