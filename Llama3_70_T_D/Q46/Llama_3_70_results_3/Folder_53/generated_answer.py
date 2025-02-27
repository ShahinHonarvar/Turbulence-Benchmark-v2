def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[66], nums[56], nums[92])
    return gcf(gcf(a, b), c)