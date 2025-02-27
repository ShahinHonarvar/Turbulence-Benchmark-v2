def return_binary_or_hexa(tuple_):
    a = tuple_[57]
    b = tuple_[84]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in tuple_[57:85]:
            sum_ += i
    if sum_ == 0:
        return ''
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]