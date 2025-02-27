def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[22]
    b = nums[97]
    c = nums[64]
    return gcf(gcf(a, b), c)