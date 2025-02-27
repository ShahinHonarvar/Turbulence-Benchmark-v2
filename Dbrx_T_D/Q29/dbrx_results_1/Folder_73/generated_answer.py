def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2 = (nums[27], nums[51])
    return gcd(num1, num2) if num1 > 0 and num2 > 0 else 0