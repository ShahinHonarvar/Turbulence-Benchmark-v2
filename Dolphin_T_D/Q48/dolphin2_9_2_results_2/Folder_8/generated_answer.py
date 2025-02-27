def return_binary_or_hexa(num_tuple):
    a = num_tuple[45]
    b = num_tuple[48]
    sum_ = 0
    for i in range(a + 1, b):
        if not num_tuple[45:49].__contains__(i):
            sum_ += i
    if sum_ % 2:
        return bin(sum_).replace('0b', '')
    else:
        return hex(sum_).replace('0x', '')