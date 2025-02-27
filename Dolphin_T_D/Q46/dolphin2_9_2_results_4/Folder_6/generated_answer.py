def gcf_three_nums(nums):
    num1 = nums[93]
    num2 = nums[94]
    num3 = nums[57]

    def gcd(a, b):
        while b != 0:
            temp = a
            a = b
            b = temp % b
        return a
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf