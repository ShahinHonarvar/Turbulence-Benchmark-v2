def sum_in_range(list_nums):
    sum_nums = 0
    for num in list_nums:
        if num >= 50 and num <= 92:
            sum_nums += num
    if sum_nums == 0:
        return 0
    return sum_nums