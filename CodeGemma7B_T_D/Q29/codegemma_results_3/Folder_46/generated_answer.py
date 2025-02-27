def gcf_two_nums(nums):
    a, b = (nums[36], nums[54])
    while b:
        a, b = (b, a % b)
    return a