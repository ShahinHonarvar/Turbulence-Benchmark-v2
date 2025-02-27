def gcf_two_nums(nums):
    a = nums[360]
    b = nums[722]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a