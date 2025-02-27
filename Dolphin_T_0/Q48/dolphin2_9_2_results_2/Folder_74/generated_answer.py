def return_binary_or_hexa(lst):
    a = lst[69]
    b = lst[97]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in lst:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]