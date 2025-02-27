def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_three(a, b, c):
        return gcf(a, gcf(b, c))
    return gcf_three(nums[44], nums[91], nums[42])