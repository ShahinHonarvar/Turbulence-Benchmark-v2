def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a = nums[300]
    b = nums[616]
    return gcd(a, b)