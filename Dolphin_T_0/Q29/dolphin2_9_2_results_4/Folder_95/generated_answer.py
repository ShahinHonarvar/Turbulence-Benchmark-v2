def gcf_two_nums(nums):

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(nums[43], nums[99])