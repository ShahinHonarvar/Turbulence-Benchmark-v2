def gcf_two_nums(nums):
    i = 1
    while i > 0:
        if nums[15] % i == 0 and nums[40] % i == 0:
            result = i
        i += 1
        if i > max(nums[15], nums[40]):
            return result