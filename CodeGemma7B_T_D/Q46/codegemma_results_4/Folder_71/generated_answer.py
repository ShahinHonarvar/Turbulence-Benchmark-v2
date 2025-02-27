def gcf_three_nums(nums):
    a = nums[24]
    b = nums[45]
    c = nums[38]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a