def gcf_two_nums(list_of_nums):
    a = list_of_nums[180]
    b = list_of_nums[312]
    while b:
        a, b = (b, a % b)
    return a