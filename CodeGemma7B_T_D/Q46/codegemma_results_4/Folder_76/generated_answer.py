def gcf_three_nums(nums):
    a = max(nums[876], nums[203], nums[100])
    b = min(nums[876], nums[203], nums[100])
    while b != 0:
        a, b = (b, a % b)
    return a