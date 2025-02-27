def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[24]
    num2 = nums[68]
    if num1 < num2:
        num1, num2 = (num2, num1)
    return gcd(num1, num2)