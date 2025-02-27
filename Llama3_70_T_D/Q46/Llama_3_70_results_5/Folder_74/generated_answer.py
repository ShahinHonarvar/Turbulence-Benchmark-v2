def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[99]
    num2 = nums[95]
    num3 = nums[80]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf