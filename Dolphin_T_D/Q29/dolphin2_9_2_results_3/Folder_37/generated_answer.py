def gcf_two_nums(nums):
    a = nums[29]
    b = nums[74]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a