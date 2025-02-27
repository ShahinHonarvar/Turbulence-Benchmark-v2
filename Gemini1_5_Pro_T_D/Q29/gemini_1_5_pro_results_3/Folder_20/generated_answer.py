def gcf_two_nums(list_of_nums):
    a = list_of_nums[19]
    b = list_of_nums[94]
    while b:
        a, b = (b, a % b)
    return a