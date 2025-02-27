def gcf_three_nums(nums):
    a = nums[876]
    b = nums[203]
    c = nums[100]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(a, b), c)