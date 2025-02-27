def gcf_two_nums(nums):
    a = nums[38]
    b = nums[77]
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a