def return_binary_or_hexa(tuple_):
    a = tuple_[10]
    b = tuple_[76]
    set_ = set(range(a + 1, b)) - set_(tuple_[10:77])
    sum_ = sum(set_)
    if sum_ % 2:
        return bin(sum_)[2:]
    return hex(sum_)[2:].upper() if sum_ > 9 else hex(sum_)[2:]