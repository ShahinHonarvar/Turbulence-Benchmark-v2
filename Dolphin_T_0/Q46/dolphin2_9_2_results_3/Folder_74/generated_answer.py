def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[99], nums[95], nums[80])
    gcf_ab = gcf(a, b)
    gcf_abc = gcf(gcf_ab, c)
    return gcf_abc