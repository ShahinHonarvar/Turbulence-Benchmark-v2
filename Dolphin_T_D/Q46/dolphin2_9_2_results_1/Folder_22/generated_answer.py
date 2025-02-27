def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums = nums[27:86:51]
    gcf = nums[0]
    for num in nums[1:]:
        gcf = gcd(gcf, num)
    return gcf