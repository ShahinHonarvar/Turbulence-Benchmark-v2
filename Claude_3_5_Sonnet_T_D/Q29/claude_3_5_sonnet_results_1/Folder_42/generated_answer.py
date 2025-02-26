def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 91:
        return None
    num1 = nums[90]
    num2 = nums[84]
    return gcd(num1, num2)