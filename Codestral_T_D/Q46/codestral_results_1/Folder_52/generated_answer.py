def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_ab = gcf(nums[19], nums[49])
    gcf_abc = gcf(gcf_ab, nums[74])
    return gcf_abc