def gcf_three_nums(nums):
    num1 = nums[1]
    num2 = nums[2]
    num3 = nums[7]

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(gcd(num1, num2), num3)