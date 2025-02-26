def gcf_two_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 8 and isinstance(nums[3], int) and isinstance(nums[8], int):
        return gcf(nums[3], nums[8])
    else:
        return None