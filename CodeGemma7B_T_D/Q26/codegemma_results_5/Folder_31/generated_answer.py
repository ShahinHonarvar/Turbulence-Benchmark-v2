def sum_in_range(list_of_nums):
    sum_of_nums = 0
    for num in list_of_nums:
        if num >= 60 and num <= 97:
            sum_of_nums += num
    return sum_of_nums