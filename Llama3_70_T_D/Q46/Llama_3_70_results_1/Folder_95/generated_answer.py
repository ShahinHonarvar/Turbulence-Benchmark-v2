def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_1_2 = gcf(nums[87], nums[20])
    return gcf(gcf_1_2, nums[36])