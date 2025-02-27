def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[70]
    num2 = nums[41]
    num3 = nums[20]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf