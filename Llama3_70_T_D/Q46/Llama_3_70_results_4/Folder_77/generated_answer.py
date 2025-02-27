def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf_693_331 = gcf(nums[693], nums[331])
    return gcf(gcf_693_331, nums[668])