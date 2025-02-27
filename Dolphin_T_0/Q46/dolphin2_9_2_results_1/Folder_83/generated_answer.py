def gcf_three_nums(nums):
    num1 = nums[56]
    num2 = nums[54]
    num3 = nums[13]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    result = gcd(num1, num2)
    result = gcd(result, num3)
    return result