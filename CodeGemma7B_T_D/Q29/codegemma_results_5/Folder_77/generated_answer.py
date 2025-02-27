def gcf_two_nums(nums):

    def gcd(a, b):
        return b if a % b == 0 else gcd(b, a % b)
    return gcd(nums[841], nums[804])