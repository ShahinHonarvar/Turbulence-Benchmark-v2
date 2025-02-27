def gcf_three_nums(nums):
    a = nums[0]
    b = nums[7 if len(nums) > 7 else 0]
    c = nums[9 if len(nums) > 9 else 0]
    while b:
        a, b = (b, a % b)
    gcf = a
    while c:
        gcf, c = (c, gcf % c)
    while gcf % b:
        gcf = gcf - b
    return gcf