def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    existing_nums = set(t[74:84])
    sum_of_missing_nums = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if sum_of_missing_nums == 0:
        return ''
    elif sum_of_missing_nums % 2 == 1:
        return bin(sum_of_missing_nums)[2:]
    else:
        return hex(sum_of_missing_nums)[2:]