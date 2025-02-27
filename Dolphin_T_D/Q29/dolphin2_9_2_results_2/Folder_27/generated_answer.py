def gcf_two_nums(nums):
    a = nums[15]
    b = nums[40]
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcf_two_nums([a % b] + nums)
    else:
        return gcf_two_nums([b % a] + nums)