def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 47 and len(nums) > 10:
        return gcd(nums[47], nums[10])
    else:
        return None