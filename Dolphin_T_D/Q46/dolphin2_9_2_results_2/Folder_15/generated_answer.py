def gcf_three_nums(nums):
    a = nums[4]
    b = nums[0]
    c = nums[8]
    if a < b:
        a, b = (b, a)
    if b < c:
        b, c = (c, b)
    if a < b:
        a, b = (b, a)
    gcf = a
    while b != 0:
        gcf = b
        b = a % b
        a = gcf
    return gcf