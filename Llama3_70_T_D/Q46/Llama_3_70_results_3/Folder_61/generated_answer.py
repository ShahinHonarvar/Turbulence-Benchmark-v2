def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a = nums[1]
    b = nums[2]
    c = nums[7]
    gcf_ab = gcf(a, b)
    return gcf(gcf_ab, c)