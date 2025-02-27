def gcf_three_nums(nums):
    a = nums[63]
    b = nums[73]
    c = nums[11]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(a, b), c)