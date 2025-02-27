def gcf_three_nums(nums):
    a = nums[1]
    b = nums[6]
    c = nums[8]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(a, gcf(b, c))