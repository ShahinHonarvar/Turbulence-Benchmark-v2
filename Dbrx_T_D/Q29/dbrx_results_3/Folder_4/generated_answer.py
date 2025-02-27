def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[76]
    num2 = nums[57]
    if num1 < 0 or num2 < 0:
        raise ValueError('Both numbers must be positive.')
    return gcd(num1, num2) if num1 < num2 else gcd(num2, num1)