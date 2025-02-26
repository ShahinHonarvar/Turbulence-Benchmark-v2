def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 96:
        return None
    num1 = nums[92]
    num2 = nums[69]
    num3 = nums[95]
    first_gcd = gcd(num1, num2)
    return gcd(first_gcd, num3)