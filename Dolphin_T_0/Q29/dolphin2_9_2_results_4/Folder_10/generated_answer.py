def gcf_two_nums(nums):

    def gfc(a, b):
        if a % b == 0:
            return b
        else:
            return gfc(b, a % b)
    return gfc(nums[15], nums[99])