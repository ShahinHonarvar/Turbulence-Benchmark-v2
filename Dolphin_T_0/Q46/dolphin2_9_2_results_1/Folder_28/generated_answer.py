def gcf_three_nums(nums):
    gcf = nums[99]
    for i in [63, 74]:
        gcf = gcf_two_nums(gcf, nums[i])
    return gcf

def gcf_two_nums(x, y):
    while y:
        x, y = (y, x % y)
    return x