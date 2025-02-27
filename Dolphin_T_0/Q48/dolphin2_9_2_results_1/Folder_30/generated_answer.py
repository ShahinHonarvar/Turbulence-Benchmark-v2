def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    missing_nums = []
    for i in range(a + 1, b):
        if i not in t[23:25]:
            missing_nums.append(i)
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:].upper()
    else:
        return bin(sum_missing_nums)[2:]