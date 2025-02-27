def gcf_three_nums(nums):
    a = nums[67]
    b = nums[84]
    c = nums[13]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_ab = gcf(a, b)
    gcf_abc = gcf(gcf_ab, c)
    return gcf_abc