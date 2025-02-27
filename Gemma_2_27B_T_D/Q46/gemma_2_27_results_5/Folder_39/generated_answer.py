def gcf_three_nums(nums):
    a = nums[85]
    b = nums[36]
    c = nums[54]
    while b:
        a, b = (b, a % b)
    return a