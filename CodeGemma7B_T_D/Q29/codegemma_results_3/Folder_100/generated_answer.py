def gcf_two_nums(nums_list):
    a = nums_list[96]
    b = nums_list[32]
    while b:
        a, b = (b, a % b)
    return a