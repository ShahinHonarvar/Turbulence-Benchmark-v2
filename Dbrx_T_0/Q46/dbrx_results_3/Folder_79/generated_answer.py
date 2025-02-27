def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[16]
    num2 = nums[87]
    num3 = nums[95]
    return gcd(num1, gcd(num2, num3))