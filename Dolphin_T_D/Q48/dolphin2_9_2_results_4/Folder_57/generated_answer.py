def return_binary_or_hexa(lst):
    if len(lst) < 81:
        return ''
    a = lst[25]
    b = lst[80]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in lst:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]