def gcf_three_nums(nums):
    return gcf(nums[20], gcf(nums[35], nums[74]))

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a