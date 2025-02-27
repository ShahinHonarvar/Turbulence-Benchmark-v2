def sum_in_range(list_of_nums):
    sum_of_valid_nums = 0
    for num in list_of_nums:
        if -358 <= num <= 185:
            sum_of_valid_nums += num
    return sum_of_valid_nums