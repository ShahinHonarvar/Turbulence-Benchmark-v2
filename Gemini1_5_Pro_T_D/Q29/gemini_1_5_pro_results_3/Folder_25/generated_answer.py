def gcf_two_nums(list_of_nums):
    a = list_of_nums[41]
    b = list_of_nums[69]
    while b:
        a, b = (b, a % b)
    return a