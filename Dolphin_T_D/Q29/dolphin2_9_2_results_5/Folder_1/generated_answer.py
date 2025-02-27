def gcf_two_nums(nums):
    num1 = nums[13]
    num2 = nums[66]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(num1, num2)