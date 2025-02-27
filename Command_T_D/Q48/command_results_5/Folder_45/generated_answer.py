def return_binary_or_hexa(test_tup):
    test_tup.sort()
    a = test_tup[30]
    b = test_tup[200]
    sum_ = b - a - 1
    if sum_ % 2 == 1:
        return '{:b}'.format(sum_)
    else:
        return '{:x}'.format(sum_)