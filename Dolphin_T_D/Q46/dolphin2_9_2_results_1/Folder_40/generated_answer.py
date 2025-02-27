def gcf_three_nums(nums):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    idx1 = nums[1]
    idx6 = nums[6]
    idx8 = nums[8]
    return gcf(gcf(idx1, idx6), idx8)