def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[1]
    b = nums[2]
    c = nums[7]
    return gcf(gcf(a, b), c)