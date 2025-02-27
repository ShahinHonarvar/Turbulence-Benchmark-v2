def return_binary_or_hexa(tup):
    beg = tup[56] + 1
    end = tup[90] - 1
    sum_of_missing_nums = 0
    for num in range(beg, end + 1):
        if num not in tup[56:91]:
            sum_of_missing_nums += num
    if sum_of_missing_nums % 2 == 0:
        return format(sum_of_missing_nums, 'x')
    else:
        return format(sum_of_missing_nums, 'b')