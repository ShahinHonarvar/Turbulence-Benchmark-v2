def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def gcf_three(a, b, c):
        return gcf(gcf(a, b), c)
    return gcf_three(nums[76], nums[35], nums[74])