def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums_list):
    nums = [nums_list[24], nums_list[25], nums_list[80]]
    return gcf(gcf(nums[0], nums[1]), nums[2])