def gcf_three_nums(nums):
    a = nums[145]
    b = nums[183]
    c = nums[770]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a