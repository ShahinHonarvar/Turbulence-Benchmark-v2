def gcf_three_nums(nums):
    a = nums[67]
    b = nums[84]
    c = nums[13]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a