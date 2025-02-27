def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    n1, n2, n3 = (nums[93], nums[94], nums[57])
    return gcf(gcf(n1, n2), n3)