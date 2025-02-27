def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums_to_consider = [nums[29], nums[53], nums[42]]
    return reduce(gcd, nums_to_consider)