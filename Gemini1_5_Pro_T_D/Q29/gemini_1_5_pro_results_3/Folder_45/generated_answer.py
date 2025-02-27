def gcf_two_nums(nums):
    a = nums[47]
    b = nums[97]
    while a:
        a, b = (b % a, a)
    return b