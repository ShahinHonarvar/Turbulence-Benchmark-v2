def gcf_two_nums(nums):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    return gcf(nums[15], nums[40])