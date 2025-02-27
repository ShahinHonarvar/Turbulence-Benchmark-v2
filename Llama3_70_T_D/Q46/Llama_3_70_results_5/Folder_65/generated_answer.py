def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 76:
        return gcf(gcf(nums[18], nums[10]), nums[76])
    else:
        return None