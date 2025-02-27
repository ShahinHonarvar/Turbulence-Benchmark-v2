def gcf_two_nums(nums):
    a = nums[13]
    b = nums[66]

    def gcd(a, b):
        while a != 0:
            a, b = (b % a, a)
        return b
    return gcd(a, b)