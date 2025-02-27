def gcf_two_nums(nums):
    a = nums[634]
    b = nums[585]
    while b:
        a, b = (b, a % b)
    return a