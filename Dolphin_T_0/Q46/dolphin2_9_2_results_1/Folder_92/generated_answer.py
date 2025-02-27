def gcf_three_nums(nums):
    a = nums[7]
    b = nums[9]
    c = nums[0]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_ab = gcf(a, b)
    gcf_abc = gcf(gcf_ab, c)
    return gcf_abc