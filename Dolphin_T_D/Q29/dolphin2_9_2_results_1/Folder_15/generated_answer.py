def gcf_two_nums(nums):
    if len(nums) < 2:
        return 0
    a = nums[0]
    b = nums[1]
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a