def gcf_three_nums(nums):
    if not isinstance(nums, list) or len(nums) < 29:
        raise ValueError('Input must be a list with length >= 29')
    num1, num2, num3 = (nums[20], nums[17], nums[28])
    if not num1 > 0 or not num2 > 0 or (not num3 > 0):
        raise ValueError('All list elements must be positive integers')

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    return gcd(lcm(num1, num2), num3)