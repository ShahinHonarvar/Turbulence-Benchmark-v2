def return_binary_or_hexa(tuple_):
    a = tuple_[43]
    b = tuple_[70]
    sum_ = sum(set(range(a + 1, b)) - set(tuple_[43:71]))
    if sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]