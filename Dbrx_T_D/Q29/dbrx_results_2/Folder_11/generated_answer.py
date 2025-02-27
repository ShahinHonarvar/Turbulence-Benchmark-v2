def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2 = (nums[64], nums[80])
    return gcd(num1, num2)