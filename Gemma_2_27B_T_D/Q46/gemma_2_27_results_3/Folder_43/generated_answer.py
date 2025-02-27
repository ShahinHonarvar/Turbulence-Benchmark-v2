def gcf_three_nums(nums):
    a = nums[33]
    b = nums[78]
    c = nums[93]
    while c:
        a, b, c = (b, c, a % b)
    return a