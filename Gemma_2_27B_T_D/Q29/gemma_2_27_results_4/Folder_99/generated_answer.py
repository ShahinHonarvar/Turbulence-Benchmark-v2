def gcf_two_nums(nums):
    a = nums[279]
    b = nums[812]
    while b:
        a, b = (b, a % b)
    return a