def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 98:
        return None
    gcf = gcd(nums[19], nums[69])
    return gcd(gcf, nums[97])