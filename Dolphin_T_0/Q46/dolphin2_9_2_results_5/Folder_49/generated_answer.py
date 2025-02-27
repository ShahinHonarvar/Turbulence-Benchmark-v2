def gcf_three_nums(nums):
    num1 = nums[34]
    num2 = nums[38]
    num3 = nums[77]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num1, num2), num3)