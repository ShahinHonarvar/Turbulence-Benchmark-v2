def gcf_three_nums(nums):
    if len(nums) < 3:
        return 'Input list must have at least three elements.'

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[21]
    num2 = nums[69]
    num3 = nums[41]
    gcf12 = gcd(num1, num2)
    gcf = gcd(gcf12, num3)
    return gcf