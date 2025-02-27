def gcf_two_nums(nums):
    a = nums[165]
    b = nums[105]
    while b != 0:
        a, b = (b, a % b)
    return a