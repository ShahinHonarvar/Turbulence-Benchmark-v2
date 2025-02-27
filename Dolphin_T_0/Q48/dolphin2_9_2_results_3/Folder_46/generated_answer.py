def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[79]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    elif sum_ != 0:
        return hex(sum_)[2:].upper()
    else:
        return ''