def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    first = nums[17]
    second = nums[88]
    third = nums[35]
    return gcd(first, gcd(second, third))