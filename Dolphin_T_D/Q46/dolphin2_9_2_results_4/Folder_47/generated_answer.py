def gcf_three_nums(nums):
    a = nums[36]
    b = nums[85]
    c = nums[83]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(a, gcf(b, c))