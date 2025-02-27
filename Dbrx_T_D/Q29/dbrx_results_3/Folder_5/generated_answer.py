def gcf_two_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    return gcf(nums[23], nums[45])