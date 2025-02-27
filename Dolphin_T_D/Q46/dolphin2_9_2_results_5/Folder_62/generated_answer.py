def gcf_three_nums(nums):
    a = nums[10]
    b = nums[55]
    c = nums[36]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(a, b), c)