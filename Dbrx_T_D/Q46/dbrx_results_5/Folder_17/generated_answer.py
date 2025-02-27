def gcf_three_nums(nums):
    if len(nums) < 3:
        return 1
    num1 = nums[20]
    num2 = nums[51]
    num3 = nums[62]

    def gcd(a, b):
        return gcd(b, a % b) if a % b else b

    def lcm(a, b):
        return a * b // gcd(a, b)
    gcf = gcd(num1, gcd(num2, num3))
    return gcf