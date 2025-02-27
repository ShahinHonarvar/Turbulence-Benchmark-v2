def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    index27, index34 = (nums[27], nums[34])
    return gcd(index27, index34)