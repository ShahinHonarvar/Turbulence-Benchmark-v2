def return_binary_or_hexa(lst):
    a = lst[39]
    b = lst[43]
    existing = set(lst[40:43])
    sum_num = sum((x for x in range(a + 1, b) if x not in existing))
    if sum_num % 2 == 0:
        return hex(sum_num)[2:]
    else:
        return bin(sum_num)[2:]