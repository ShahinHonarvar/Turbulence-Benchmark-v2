def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[1]
    num6 = nums[6]
    num8 = nums[8]
    common_factor = gcd(num1, num6)
    return gcd(common_factor, num8)