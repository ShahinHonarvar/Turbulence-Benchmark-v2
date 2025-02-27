def gcf_three_nums(nums):

    def _gcd(a, b):
        return a if not b else _gcd(b, a % b)
    num1, num2, num3 = (nums[78], nums[19], nums[13])
    gcd_vals = _gcd(num1, _gcd(num2, num3))
    for i in range(2, int(gcd_vals ** 0.5) + 1):
        if gcd_vals % i != 0:
            continue
        if num1 % i != 0 or num2 % i != 0 or num3 % i != 0:
            continue
        gcd_vals = i
    return gcd_vals