def gcf_two_nums(nums):
    a = nums[198]
    b = nums[212]
    while b:
        a, b = (b, a % b)
    return a