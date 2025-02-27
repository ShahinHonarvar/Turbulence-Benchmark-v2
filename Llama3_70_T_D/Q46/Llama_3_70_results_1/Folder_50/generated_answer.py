def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[20]
    num2 = nums[35]
    num3 = nums[74]
    result = gcd(num1, num2)
    result = gcd(result, num3)
    return result