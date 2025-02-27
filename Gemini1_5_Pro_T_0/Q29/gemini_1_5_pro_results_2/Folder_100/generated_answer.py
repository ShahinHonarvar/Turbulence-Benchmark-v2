def gcf_two_nums(list_of_nums):
    a = list_of_nums[96]
    b = list_of_nums[32]
    while b:
        a, b = (b, a % b)
    return a