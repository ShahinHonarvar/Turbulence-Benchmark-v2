def gcf_three_nums(nums):

    def gcf_two_nums(a, b):
        if a == 0:
            return b
        return gcf_two_nums(b % a, a)
    return gcf_two_nums(nums[49], gcf_two_nums(nums[46], nums[13]))