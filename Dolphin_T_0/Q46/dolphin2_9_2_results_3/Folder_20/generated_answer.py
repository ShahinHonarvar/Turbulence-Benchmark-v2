def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_val = gcf(nums[29], nums[53])
    gcf_val = gcf(gcf_val, nums[42])
    return gcf_val