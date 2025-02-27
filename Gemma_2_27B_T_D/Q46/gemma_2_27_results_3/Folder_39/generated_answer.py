def gcf_three_nums(nums):
    a = nums[85]
    b = nums[36]
    c = nums[54]
    while c:
        a, b, c = (b, c, a % c)
    return a