def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (nums[92], nums[69], nums[95])
    return gcd(gcd(num1, num2), num3)