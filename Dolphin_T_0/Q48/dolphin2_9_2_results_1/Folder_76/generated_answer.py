def return_binary_or_hexa(lst):
    a = lst[450]
    b = lst[905]
    sum_ = sum((i for i in range(a + 1, b) if i not in lst[450:906]))
    if sum_ % 2 != 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]