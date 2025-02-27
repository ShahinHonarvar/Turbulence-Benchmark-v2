def return_binary_or_hexa(lst):
    a = lst[60]
    b = lst[200]
    sum_num = sum((i for i in range(a + 1, b) if i not in lst[61:200]))
    if sum_num % 2 == 0:
        return bin(sum_num)[2:]
    else:
        return hex(sum_num)[2:]