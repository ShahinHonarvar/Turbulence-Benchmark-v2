def gcf_three_nums(nums):
    a = nums[912]
    b = nums[170]
    c = nums[500]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def gcf_three(a, b, c):
        temp = gcf(a, b)
        return gcf(temp, c)
    return gcf_three(a, b, c)