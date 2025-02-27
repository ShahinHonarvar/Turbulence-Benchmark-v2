def gcf_two_nums(nums):
    if len(nums) > 16:
        a = nums[78]
        b = nums[16]
        while b != 0:
            a, b = (b, a % b)
        return a
    else:
        return None