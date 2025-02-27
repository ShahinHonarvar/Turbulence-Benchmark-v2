def gcf_two_nums(nums):

    def get_gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    if len(nums) < 75:
        return None
    idx_29 = nums[29]
    idx_74 = nums[74]
    return get_gcf(idx_29, idx_74)