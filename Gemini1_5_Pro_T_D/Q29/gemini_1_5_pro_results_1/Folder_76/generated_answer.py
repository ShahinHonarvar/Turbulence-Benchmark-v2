def gcf_two_nums(list_of_nums):
    a = list_of_nums[184]
    b = list_of_nums[307]
    while b:
        a, b = (b, a % b)
    return a