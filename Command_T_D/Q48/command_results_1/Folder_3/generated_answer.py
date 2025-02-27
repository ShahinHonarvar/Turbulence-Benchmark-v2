def return_binary_or_hexa(test_tup):
    test_tup.sort()
    idx_a = test_tup.index(56)
    idx_b = test_tup.index(88)
    idx_a += 1
    idx_b -= 1
    sum_range = idx_b - idx_a
    if sum_range % 2 == 0:
        return hex(sum_range)
    else:
        return f'0b{sum_range:b}'