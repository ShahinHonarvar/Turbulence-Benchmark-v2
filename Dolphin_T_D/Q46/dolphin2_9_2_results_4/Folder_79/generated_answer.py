def gcf_three_nums(nums):
    a = nums[16]
    b = nums[87]
    c = nums[95]

    def gcf(a, b, c):
        if a == 0:
            return b // c
        return gcf(b % a, c, a)
    return gcf(a, b, c)