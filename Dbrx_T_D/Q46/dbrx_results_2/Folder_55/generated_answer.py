def gcf_three_nums(nums):
    if not all((isinstance(num, int) and num > 0 for num in nums)):
        raise ValueError('All elements in the list must be positive integers')
    num1, num2, num3 = (nums[9], nums[6], nums[2])
    for num in [num1, num2, num3]:
        if not (isinstance(num, int) and num > 0):
            raise ValueError('All elements in the list must be positive integers')

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    gcf = gcd(num1, gcd(num2, num3))
    lcm_val = lcm(num1, lcm(num2, num3))
    if gcf == 1:
        return lcm_val
    else:
        return gcf