def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[99]
    num2 = nums[63]
    num3 = nums[74]
    gcf_1_2 = gcd(num1, num2)
    return gcd(gcf_1_2, num3)