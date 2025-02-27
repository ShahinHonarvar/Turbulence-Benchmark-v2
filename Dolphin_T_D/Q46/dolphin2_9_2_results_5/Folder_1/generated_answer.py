def gcf_three_nums(list_of_nums):
    nums = [list_of_nums[74], list_of_nums[51], list_of_nums[27]]
    return gcf(gcf(nums[0], nums[1]), nums[2])

def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)