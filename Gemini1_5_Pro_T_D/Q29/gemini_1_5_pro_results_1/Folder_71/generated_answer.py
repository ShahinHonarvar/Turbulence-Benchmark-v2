def gcf_two_nums(nums):
    a = nums[78]
    b = nums[93]
    while b:
        a, b = (b, a % b)
    return a